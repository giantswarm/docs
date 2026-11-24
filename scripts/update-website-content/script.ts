import { chromium } from "playwright";
import type { Page } from "playwright";
import fs from "fs/promises";
import path from "path";
import https from "https";

const websiteURL = "https://www.giantswarm.io/privacy-policy";

// The website renders the header twice, once in a static host and once in a
// sticky host that takes over on scroll. The docs site keeps its header in
// place, so it takes the static host, which content pages render solid.
const headerHostSelector = ".gs-header-host--static";

// The mobile drawer and the search overlay are siblings of the header on the
// website. The docs site needs all three in the same shadow root.
const mobileMenuSelector = ".gs-mobile-menu";
const searchOverlaySelector = ".gs-search";

// Marks the sample search result that search-modal.html carries only so that
// the website's result rules have something to match.
const sampleSelector = "[data-sample]";

const footerElementSelector = "footer.gs-footer";
const cookiesBannerElementSelector = "#hs-eu-cookie-confirmation";

// The language switcher points at translated pages that only exist on the
// marketing site, so the docs copy drops it.
const languageSwitcherSelectors = [".gs-nav__item--lang", ".gs-mobile-menu__lang"];

const sectionTemplatesPath = path.join(
  import.meta.dirname,
  "..",
  "..",
  "src",
  "layouts",
  "partials"
);
const headerPath = path.join(sectionTemplatesPath, "gs_header.html");
const headerStylesPath = path.join(sectionTemplatesPath, "gs_header_styles.html");
const footerPath = path.join(sectionTemplatesPath, "gs_footer.html");
const footerStylesPath = path.join(sectionTemplatesPath, "gs_footer_styles.html");
const cookiesBannerStylesPath = path.join(sectionTemplatesPath, "gs_cookies_banner_styles.html");

const cssOverridesPath = path.join(import.meta.dirname, "overrides.css");
const searchModalPath = path.join(import.meta.dirname, "search-modal.html");

const generatedFileDisclaimer =
  "<!-- !!! DO NOT EDIT !!! File generated with 'make update-website-content' -->";

(async () => {
  log("Templating website content started.\n");

  log("Opening browser.");

  const browser = await chromium.launch();
  const context = await browser.newContext({
    viewport: { width: 1920, height: 1080 },
    deviceScaleFactor: 2,
  });

  log(`Opening ${websiteURL}.`);
  const page = await context.newPage();
  await page.goto(websiteURL);

  await page.waitForLoadState("load");
  log("Page loaded successfully.");

  log("Setting up environment.");

  // Expose a custom function for fetching text files, to not have to deal with CORS issues.
  await page.exposeFunction("fetchTextFile", fetchTextFile);

  // Everything below changes the page before anything is read from it, so that
  // what gets written out is already what the docs site needs.
  log("Adapting the page for the docs site.");
  await makeLinksAbsolute(page);
  await removeElements(page, languageSwitcherSelectors);
  await installSearchContents(page, (await fs.readFile(searchModalPath)).toString().trim());

  // Header, mobile drawer and search overlay.
  log("Extracting header contents.");
  const headerHost = await extractElementContents(page, headerHostSelector);
  const mobileMenu = await extractElementContents(page, mobileMenuSelector);

  // The CSS comes first, while the sample result is still in the overlay. It
  // is there for the website's result rules to match, and nothing more, so it
  // goes away before the markup is read.
  const searchCSS = await extractElementCSS(page, searchOverlaySelector);
  await removeElements(page, [sampleSelector]);
  const searchHTML = await extractElementHTML(page, searchOverlaySelector);

  log("Writing header HTML.");
  await writeGeneratedFile(headerPath, [...headerHost.html, ...mobileMenu.html, ...searchHTML].join("\n"));

  log("Writing header CSS.");
  const headerCSS = forShadowRoot([...headerHost.css, ...mobileMenu.css, ...searchCSS]);
  const headerCSSWithOverrides = await applyCSSOverrides(headerCSS);
  await writeGeneratedFile(headerStylesPath, `<style>\n${headerCSSWithOverrides.join("\n")}\n</style>`);

  // Footer.
  log("Extracting footer contents.");
  const footer = await extractElementContents(page, footerElementSelector);

  log("Writing footer HTML.");
  await writeGeneratedFile(footerPath, footer.html.join(""));

  log("Writing footer CSS.");
  const footerCSS = forShadowRoot(footer.css);
  await writeGeneratedFile(footerStylesPath, `<style>\n${footerCSS.join("\n")}\n</style>`);

  // Cookie Consent Banner.
  log("Extracting cookies consent banner contents.");
  const cookiesBannerElement = await extractElementContents(page, cookiesBannerElementSelector);
  const cookiesBanner = processCookiesBannerContents(cookiesBannerElement);

  log("Writing cookies consent banner CSS file.");
  // The banner is the one part that renders outside a shadow root, so its
  // tokens stay on :root.
  const cookiesBannerCSS = Array.from(new Set(cookiesBanner.css));
  await writeGeneratedFile(
    cookiesBannerStylesPath,
    `<style>\n${cookiesBannerCSS.join("\n")}\n</style>`
  );

  log("Closing browser.");
  await browser.close();

  log("\nTemplating website content finished successfully.");
})();

interface ElementContents {
  html: string[];
  css: string[];
}

/**
 * Turn every link on the page into an absolute one. The website serves its own
 * links as paths, which would resolve against docs.giantswarm.io. The hsLang
 * parameter goes with them, since it pins a language the docs site has not got.
 */
async function makeLinksAbsolute(page: Page): Promise<void> {
  await page.evaluate(() => {
    for (const link of document.querySelectorAll("a[href]")) {
      // The href property is already resolved against the page's own URL.
      const url = new URL((link as HTMLAnchorElement).href);
      url.searchParams.delete("hsLang");
      link.setAttribute("href", url.toString());
    }
  });
}

/**
 * Remove every element matching one of the selectors from the page.
 */
async function removeElements(page: Page, selectors: string[]): Promise<void> {
  await page.evaluate((list) => {
    for (const selector of list) {
      for (const element of document.querySelectorAll(selector)) {
        element.remove();
      }
    }
  }, selectors);
}

/**
 * Put the docs search markup into the website's search overlay. The website
 * fills the overlay with its own results at runtime, so without this the
 * extracted CSS would miss every rule that styles a result.
 */
async function installSearchContents(page: Page, contents: string): Promise<void> {
  await page.evaluate(
    ({ selector, contents }) => {
      const overlay = document.querySelector(selector);
      if (!overlay) throw new Error(`Could not find the search overlay (${selector}).`);

      // The website ships the pages it searches as inline JSON. The docs search
      // queries an API instead, and the index is large, so it goes.
      overlay.querySelector("#search-index-data")?.remove();

      const body = overlay.querySelector(".gs-search__body");
      if (!body) throw new Error("Could not find the body of the search overlay.");

      body.innerHTML = contents;
    },
    { selector: searchOverlaySelector, contents }
  );
}

/**
 * Move the website's design tokens to where a shadow root can see them. They
 * are defined on :root, which matches the document element and so never
 * matches inside the shadow roots that hold the header and the footer.
 */
function forShadowRoot(css: string[]): string[] {
  return Array.from(new Set(css.map((rule) => rule.replaceAll(":root", ":host"))));
}

/**
 * Get the HTML content and the required CSS
 * for rendering an element.
 */
async function extractElementContents(
  page: Page,
  selector: string
): Promise<ElementContents> {
  return {
    html: await extractElementHTML(page, selector),
    css: await extractElementCSS(page, selector),
  };
}

async function extractElementHTML(page: Page, selector: string): Promise<string[]> {
  const element = await page.waitForSelector(selector, { state: "attached" });
  const html = await element.evaluate(extractHTMLForElement);

  await element.dispose();

  return html;
}

async function extractElementCSS(page: Page, selector: string): Promise<string[]> {
  const element = await page.waitForSelector(selector, { state: "attached" });
  const css = await page.evaluate(extractCSSForElement, element);

  await element.dispose();

  return css;
}

function extractHTMLForElement(e: Element): string[] {
  return [e.outerHTML];
}

async function extractCSSForElement(e: Element): Promise<string[]> {
  /**
   * CSS files that are hosted on an external domain have to be fetched
   * manually, since the browser doesn't allow accessing their CSS rules.
   * @param url
   */
  const fetchExternalCSSRules = async (
    url: string
  ): Promise<CSSRuleList | null> => {
    const cssContents = await (window as any).fetchTextFile(url);

    // Making the browser parse the CSS rules for us.
    const newDocument = document.implementation.createHTMLDocument("");

    const styleElement = newDocument.createElement("style");
    styleElement.textContent = cssContents;

    newDocument.body.appendChild(styleElement);

    if (!styleElement.sheet) return null;

    return styleElement.sheet.cssRules;
  };

  /**
   * Check if an element matches a given CSS selector.
   * @param e
   * @param selector
   */
  const elementMatchesSelector = (e: Element, selector: string) => {
    // If this is a direct selector for the element, we're good.
    if (e.matches(selector)) return true;

    /**
     * If this is something like a pseudo-element, or a :*-child rule,
     * we need to get a little bit more creative.
     */
    const elementSelectors = [];
    for (const className of e.classList) {
      elementSelectors.push(`.${className.trim()}`);
    }

    if (e.id) {
      elementSelectors.push(`#${e.id.trim()}`);
    }

    return elementSelectors.some((s) => selector.includes(s));
  };

  /**
   * Go through all the given rules and figure out which
   * of them apply to the provided elements.
   * @param rules
   * @param forElements
   */
  const extractCSSRules = async (
    rules: CSSRuleList,
    forElements: Element[]
  ): Promise<string[]> => {
    if (!rules) return [];

    const cssLines = [];
    const mediaQueries: Record<string, string[]> = {};

    for (const rule of rules) {
      switch (rule.type) {
        case CSSRule.STYLE_RULE: {
          const { selectorText } = rule as CSSStyleRule;

          // The design tokens are defined on :root and used all over the
          // website's CSS, but no element matches that selector, so they have
          // to be taken along on their own.
          if (selectorText.includes(":root")) {
            cssLines.push(rule.cssText);
            break;
          }

          for (const element of forElements) {
            if (elementMatchesSelector(element, selectorText)) {
              cssLines.push(rule.cssText);
            }
          }
        }

        case CSSRule.MEDIA_RULE: {
          let extractedLines = await extractCSSRules(
            (rule as CSSMediaRule).cssRules,
            forElements
          );
          if (extractedLines.length < 1) continue;

          // Avoiding duplicate lines.
          extractedLines = Array.from(new Set(extractedLines));

          const { mediaText } = (rule as CSSMediaRule).media;
          mediaQueries[mediaText] ??= [];
          mediaQueries[mediaText].push(extractedLines.join("\n"));
        }
      }
    }

    for (const [mediaText, rules] of Object.entries(mediaQueries)) {
      cssLines.push(`@media ${mediaText} {\n${rules.join("\n")}\n}`);
    }

    return cssLines;
  };

  // Get a flattened array of the element and all of its children.
  const elements = [e, ...e.querySelectorAll("*")];

  const cssLines: string[] = [];
  for (const styleSheet of document.styleSheets) {
    let cssRules: CSSRuleList;
    try {
      // This can trigger an error if the CSS file is hosted on an external domain.
      cssRules = styleSheet.cssRules;
    } catch {
      if (!styleSheet.href) continue;

      const externalCSSRules = await fetchExternalCSSRules(styleSheet.href);
      if (!externalCSSRules) continue;

      cssRules = externalCSSRules;
    }

    const parsedLines = await extractCSSRules(cssRules, elements);
    cssLines.push(...parsedLines);
  }

  return cssLines;
}

/**
 * Apply overrides to the existing CSS.
 * @param toContents
 */
async function applyCSSOverrides(toContents: string[]): Promise<string[]> {
  const overrides = await fs.readFile(cssOverridesPath);

  return [...toContents, overrides.toString().trim()];
}

async function writeGeneratedFile(
  toPath: string,
  contents: string
): Promise<void> {
  const patchedContents = `${generatedFileDisclaimer}\n\n${contents}\n`;

  await fs.writeFile(toPath, patchedContents);
}

async function fetchTextFile(fromURL: string): Promise<string> {
  return new Promise((resolve, reject) => {
    const req = https.get(fromURL, (res) => {
      const chunks: string[] = [];

      res.on("data", (chunk) => chunks.push(chunk));
      res.on("end", () => resolve(chunks.join("")));
    });

    req.on("error", (e) => reject(e));
  });
}

function log(message: string) {
  console.log(message);
}

function processCookiesBannerContents(header: ElementContents) {
  const { html, css } = header;
  const cleanCSS = css.filter(function(str) {
    return !(
      str.startsWith("*, ::after, ::before {") ||
      str.startsWith("a {") ||
      str.startsWith("a, a:hover {") ||
      str.startsWith(".p, blockquote, p {")
    );
  })

  return {
    html,
    css: cleanCSS,
  }
}

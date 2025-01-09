import { chromium, Page } from "playwright";
import fs from "fs/promises";
import path from "path";
import https from "https";

const websiteURL = "https://www.giantswarm.io/privacy-policy";

const headerElementSelector = "header.header";
const footerElementSelector = "footer.footer";
const cookiesBannerElementSelector = "#hs-eu-cookie-confirmation";

const sectionTemplatesPath = path.join(
  __dirname,
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

const cssOverridesPath = path.join(__dirname, "overrides.css");

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

  // Header.
  log("Extracting header contents.");
  const headerElement = await extractElementContents(page, headerElementSelector);
  const header = processHeaderContents(headerElement);

  log("Writing header HTML.");
  await writeGeneratedFile(headerPath, header.html.join(""));

  log("Writing header CSS.");
  const headerCSS = Array.from(new Set(header.css));
  const headerCSSWithOverrides = await applyCSSOverrides(headerCSS);
  await writeGeneratedFile(headerStylesPath, `<style>\n${headerCSSWithOverrides.join("\n")}\n</style>`);

  // Footer.
  log("Extracting footer contents.");
  const footer = await extractElementContents(page, footerElementSelector);

  log("Writing footer HTML.");
  await writeGeneratedFile(footerPath, footer.html.join(""));

  log("Writing footer CSS.");
  const footerCSS = Array.from(new Set(footer.css));
  await writeGeneratedFile(footerStylesPath, `<style>\n${footerCSS.join("\n")}\n</style>`);

  // Cookie Consent Banner.
  log("Extracting cookies consent banner contents.");
  const cookiesBannerElement = await extractElementContents(page, cookiesBannerElementSelector);
  const cookiesBanner = processCookiesBannerContents(cookiesBannerElement);

  log("Writing cookies consent banner CSS file.");
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
 * Get the HTML content and the required CSS
 * for rendering an element.
 */
async function extractElementContents(
  page: Page,
  selector: string
): Promise<ElementContents> {
  const element = await page.waitForSelector(selector, { state: "attached" });

  const html = await element.evaluate(extractHTMLForElement);
  const css = await page.evaluate(extractCSSForElement, element);

  await element.dispose();

  return { html, css };
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

function processHeaderContents(header: ElementContents) {
  const { html, css } = header;
  const cleanHtml = html.map(function(str) {
    return str
      .replaceAll("nav__item--active-branch", "")
      .replaceAll("nav__item--active", "")
      .replaceAll("mnav__menu__item--active-branch", "")
      .replaceAll("mnav__menu__item--active", "");
  })

  return {
    html: cleanHtml,
    css,
  }
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

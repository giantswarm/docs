import { chromium, Page } from "playwright";
import fs from "fs/promises";
import path from "path";
import https from "https";

const websiteURL = "https://www.giantswarm.io/blog";

const headerElementSelector = "header.header";
const footerElementSelector = "footer.footer";
const consentBannerElementSelector = "#hs-eu-cookie-confirmation-inner";

const sectionTemplatesPath = path.join(__dirname, "..", "..", "src", "layouts", "partials");
const stylesModulesPath    = path.join(__dirname, "..", "..", "src", "assets", "styles");

const headerPath = path.join(sectionTemplatesPath, "gs_header.html");
const footerPath = path.join(sectionTemplatesPath, "gs_footer.html");

const headerStylesPath        = path.join(stylesModulesPath, "_gs_header.scss");
const footerStylesPath        = path.join(stylesModulesPath, "_gs_footer.scss");
const consentBannerStylesPath = path.join(stylesModulesPath, "_gs_consent_banner.scss");

const cssOverridesPath = path.join(__dirname, "overrides.css");

const generatedHtmlFileDisclaimer =
  "<!-- !!! DO NOT EDIT !!! File generated with 'make update-website-content' -->";

const generatedCssFileDisclaimer =
  "/* File generated with 'make update-website-content' -- do not edit manually! */";


(async () => {
  log("Templating website content started.\n");

  log("Opening browser.");

  const browser = await chromium.launch();
  const context = await browser.newContext({
    viewport: { width: 1920, height: 1600 },
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
  log("Extracting header HTML");
  const header = await extractElementContents(page, headerElementSelector);

  log("Writing header HTML");
  await writeHtmlFile(headerPath, header.html.join(""));

  log("Writing header CSS file");
  await writeCssFile(
    headerStylesPath,
    headerElementSelector,
    header.css,
  );

  // Footer.
  log("Extracting footer HTML.");
  const footer = await extractElementContents(page, footerElementSelector);

  log("Writing footer HTML.");
  await writeHtmlFile(footerPath, footer.html.join(""));

  log("Writing footer CSS file");
  await writeCssFile(
    footerStylesPath,
    footerElementSelector,
    footer.css,
  );

  // Cookie Consent Banner.
  log("Extracting cookies consent banner HTML.");
  const consentBanner = await extractElementContents(page, consentBannerElementSelector);

  log("Writing footer CSS file");
  await writeCssFile(
    consentBannerStylesPath,
    consentBannerElementSelector,
    consentBanner.css,
  );

  log("Closing browser");
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

async function writeHtmlFile(
  toPath: string,
  contents: string
): Promise<void> {
  await fs.writeFile(toPath, `${generatedHtmlFileDisclaimer}\n\n${contents}\n`);
}

async function writeCssFile(
  toPath: string,
  prefix: string,
  styles: string[],
): Promise<void> {
  let out = generatedCssFileDisclaimer + "\n" + prefix + " {\n";
  // deduplication
  for (const style of Array.from(new Set(styles))) {
    out += "    " + style + "\n";
  }
  out += "}\n";
  await fs.writeFile(toPath, out);
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

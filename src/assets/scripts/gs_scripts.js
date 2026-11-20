const root = document.querySelector('#header').shadowRoot;
const header = root.querySelector('header');

// sticky header
const header_sticky_element = root.querySelector(".header__sticky-element");
if (header_sticky_element) {
    const header_sticky = root.querySelector(".header--sticky")
      , header_sticky_prop = header_sticky.getBoundingClientRect();
    ["resize", "scroll", "load"].forEach((function(event_type) {
        window.addEventListener(event_type, (function() {
            window.pageYOffset > header_sticky_prop.height ? (header_sticky.style.height = header_sticky_prop.height + "px",
            header_sticky.classList.add("header--sticky-active"),
            header_sticky.classList.remove("header--sticky-inactive")) : (header_sticky.classList.contains("header--sticky-active") && header_sticky.classList.add("header--sticky-inactive"),
            header_sticky.style.height = "",
            header_sticky.classList.remove("header--sticky-active"))
        }
        ))
    }
    ))
}

// mobile nav
const mobile_nav_open = root.querySelector(".mnav__open");
const mobile_nav_close = root.querySelector(".mnav__close");
const mobile_nav_popup = root.querySelector(".mnav__popup");
const mobile_nav_overlay = root.querySelector(".mnav__overlay");
const open_mobile_nav = function() {
    document.body.classList.add("mnav-active");
    header.classList.add("mnav-active");
}
const close_mobile_nav = function() {
    document.body.classList.remove("mnav-active");
    header.classList.remove("mnav-active");
};
mobile_nav_open.addEventListener("click", open_mobile_nav),
mobile_nav_close.addEventListener("click", close_mobile_nav),
mobile_nav_overlay.addEventListener("click", close_mobile_nav);
const vmenu_toggle = root.querySelectorAll('.mnav__menu__toggle, .mnav__menu__link[href="javascript:;"]');
for (i = 0; i < vmenu_toggle.length; i++) {
  vmenu_toggle[i].addEventListener("click", (function(event) {
    const vmenu_current = event.target.closest(".mnav__menu__item--parent");
    const vmenu_expanded = event.target.closest(".mnav__menu__list").querySelectorAll(":scope > .mnav__menu__item--expanded");
    for (n = 0; n < vmenu_expanded.length; n++)
      if (vmenu_expanded[n] != vmenu_current) {
        vmenu_expanded[n].classList.remove("mnav__menu__item--expanded");
        const vmenu_expanded_children = vmenu_expanded[n].querySelectorAll(".mnav__menu__item--expanded");
        for (z = 0; z < vmenu_expanded_children.length; z++) {
          vmenu_expanded_children[z].classList.remove("mnav__menu__item--expanded");
        }
      }
      event.target.closest(".mnav__menu__item").classList.toggle("mnav__menu__item--expanded");
    }
  ));
}
document.addEventListener("click", (function(e) {
  if (e.target.matches('.mnav__popup a[href*="#"]')) {
    document.body.classList.remove("mnav-active");
    header.classList.remove("mnav-active");
  }
}));

// Self-hosted docs search. The modal queries the /searchapi gateway on
// docs-proxy, which takes a few validated parameters and returns only the
// fields a result needs (see docs-proxy search.js). Everything the gateway
// returns is rendered as text, never HTML, because it comes from a public
// repo that takes outside PRs and from HubSpot.
const search_open = root.querySelector(".site-search__open");
const search_popup = root.querySelector(".site-search__popup");
const search_form = root.querySelector("#searchForm");
const search_input = root.querySelector("#searchInput");
const search_close = root.querySelector(".site-search__close");
const search_list = root.querySelector(".site-search__list");
const search_zero = root.querySelector(".site-search__results-zero");
const search_error = root.querySelector(".site-search__error");
const search_more = root.querySelector(".site-search__more");

if (search_open && search_form && search_input && search_list) {
  const SEARCH_ENDPOINT = "/searchapi/";
  const PAGE_SIZE = 10;
  const BLOG_SIZE = 4;
  const MAX_QUERY = 200;
  const MIN_QUERY = 2;
  // Groups in display order. Docs and release notes (Changes) come from one
  // query; blog posts come from a separate query so relevant ones always show.
  // The gateway scores blog far below docs, so in a mixed query blog would
  // never reach the top results. Handbook is not searched.
  const GROUP_ORDER = ["Docs", "Blog", "Changes"];

  let docsHits = [];
  let docsTotal = 0;
  let blogHits = [];
  let query = "";
  let renderedQuery = "";
  let controller = null;
  let debounce = null;
  let searchStart = 0;
  let performedTimer = null;
  let performed = null;

  // Telemetry. The query text is truncated to 100 characters to cap the payload
  // size. Truncation is not redaction: shorter tokens, emails or secrets still
  // pass through, so the query text is treated as potentially sensitive.
  function track(type, payload) {
    if (window.sendTelemetryEvent) {
      window.sendTelemetryEvent(type, payload);
    }
  }

  // "Search performed" is sent once the query settles, not on every keystroke,
  // so one logical search is one event. A result click flushes it first, so a
  // quick click still records both the search and the click.
  function flushPerformed() {
    if (performedTimer) { clearTimeout(performedTimer); performedTimer = null; }
    if (performed) {
      track("Docs.Search.Performed", performed);
      performed = null;
    }
  }

  function schedulePerformed(resultCount) {
    performed = {
      query: query.slice(0, 100),
      resultCount: resultCount,
      durationMs: Date.now() - searchStart,
    };
    if (performedTimer) clearTimeout(performedTimer);
    performedTimer = setTimeout(flushPerformed, 1500);
  }

  function escapeHtml(value) {
    return String(value)
      .replace(/&/g, "&amp;")
      .replace(/</g, "&lt;")
      .replace(/>/g, "&gt;")
      .replace(/"/g, "&quot;")
      .replace(/'/g, "&#39;");
  }

  // The gateway wraps matched terms in ** ** (its highlight tags). Escape the
  // whole string first so index content can never inject markup, then turn the
  // markers into highlight spans.
  function withHighlight(value) {
    return escapeHtml(value).replace(/\*\*([^*]+?)\*\*/g, '<span class="hs-search-highlight">$1</span>');
  }

  function safeHref(url) {
    return /^(https?:\/\/|\/)/.test(url) ? escapeHtml(url) : "#";
  }

  // A docs-query hit is either a release note (breadcrumb "changes") or a docs page.
  function docsGroupOf(source) {
    if (source.breadcrumb && source.breadcrumb[0] === "changes") return "Changes";
    return "Docs";
  }

  function openSearch() {
    search_popup.classList.add("site-search__popup--active");
    document.body.classList.add("site-search-active");
    search_input.focus();
  }

  function closeSearch() {
    flushPerformed();
    search_popup.classList.remove("site-search__popup--active");
    search_popup.classList.remove("site-search__popup--form-submitted");
    document.body.classList.remove("site-search-active");
  }

  function renderResult(hit, group, position) {
    const source = hit._source || {};
    const highlight = hit.highlight || {};
    const title = highlight.title && highlight.title[0]
      ? withHighlight(highlight.title[0])
      : escapeHtml(source.title);
    const snippet = highlight.body && highlight.body[0]
      ? withHighlight(highlight.body[0])
      : escapeHtml(source.description || "");
    let html = '<div class="site-search__result">';
    html += '<div class="site-search__result-title"><a href="' + safeHref(source.url) + '"'
      + ' data-group="' + escapeHtml(group) + '" data-pos="' + position + '">' + title + "</a></div>";
    if (snippet) {
      html += '<div class="site-search__result-desc">' + snippet + "</div>";
    }
    return html + "</div>";
  }

  function renderResults() {
    const groups = { Docs: [], Blog: [], Changes: [] };
    docsHits.forEach(function(hit) {
      groups[docsGroupOf(hit._source || {})].push(hit);
    });
    blogHits.forEach(function(hit) { groups.Blog.push(hit); });

    let html = "";
    let position = 0;
    GROUP_ORDER.forEach(function(name) {
      const items = groups[name];
      if (items.length === 0) return;
      html += '<div class="site-search__group">';
      html += '<div class="site-search__group-title">' + name + "</div>";
      items.forEach(function(hit) { position += 1; html += renderResult(hit, name, position); });
      html += "</div>";
    });

    // Remember which query these results belong to, so a click reports the
    // query that was on screen even if a newer search is already in flight.
    renderedQuery = query;
    const count = docsHits.length + blogHits.length;
    search_list.innerHTML = html;
    if (search_zero) search_zero.hidden = count > 0;
    if (search_error) search_error.hidden = true;
    if (search_more) search_more.hidden = docsHits.length >= docsTotal;
  }

  function showFallback() {
    search_list.innerHTML = "";
    if (search_zero) search_zero.hidden = true;
    if (search_more) search_more.hidden = true;
    if (search_error) {
      const url = "https://www.google.com/search?q=" + encodeURIComponent("site:docs.giantswarm.io " + query);
      search_error.innerHTML = 'Search is unavailable right now. '
        + '<a href="' + url + '" target="_blank" rel="noopener">Search on Google instead</a>.';
      search_error.hidden = false;
    }
  }

  function load(params, signal) {
    return fetch(SEARCH_ENDPOINT + "?q=" + encodeURIComponent(query) + params, {
      headers: { "Accept": "application/json" },
      signal: signal,
    }).then(function(response) {
      if (!response.ok) throw new Error("search unavailable");
      return response.json();
    });
  }

  function runSearch(append) {
    const value = search_input.value.trim().slice(0, MAX_QUERY);
    if (!append) {
      query = value;
      docsHits = [];
      docsTotal = 0;
      blogHits = [];
      searchStart = Date.now();
    }

    // Drop any in-flight request so a slower earlier query cannot render late.
    if (controller) controller.abort();
    controller = null;

    if (query.length < MIN_QUERY) {
      search_popup.classList.remove("site-search__popup--form-submitted");
      search_list.innerHTML = "";
      if (search_zero) search_zero.hidden = true;
      if (search_error) search_error.hidden = true;
      if (search_more) search_more.hidden = true;
      // The box was cleared or shortened below the minimum. A search that
      // already rendered (often a zero-result one the reader is about to
      // retype) is still worth recording, so flush it instead of dropping it.
      flushPerformed();
      return;
    }

    controller = typeof AbortController !== "undefined" ? new AbortController() : null;
    const signal = controller ? controller.signal : undefined;

    search_popup.classList.add("site-search__popup--form-submitted");

    // Docs (and release notes) in one query; a smaller blog query runs only on a
    // fresh search, so "More results" pages the docs list without refetching blog.
    const tasks = [
      load("&type=Documentation&size=" + PAGE_SIZE + "&from=" + docsHits.length, signal)
        .then(function(data) {
          const page = (data && data.hits && data.hits.hits) || [];
          docsTotal = (data && data.hits && data.hits.total && data.hits.total.value) || 0;
          docsHits = docsHits.concat(page);
        }),
    ];
    if (!append) {
      tasks.push(
        load("&type=Blog&size=" + BLOG_SIZE, signal).then(function(data) {
          blogHits = (data && data.hits && data.hits.hits) || [];
        })
      );
    }

    Promise.all(tasks)
      .then(function() {
        renderResults();
        if (!append) {
          schedulePerformed(docsHits.length + blogHits.length);
        }
      })
      .catch(function(error) {
        if (error && error.name === "AbortError") return;
        showFallback();
        // A failed "More results" page must not discard the fresh search that
        // already succeeded. Only a failed fresh search clears the pending event.
        if (!append) {
          if (performedTimer) { clearTimeout(performedTimer); performedTimer = null; }
          performed = null;
        }
        track("Docs.Search.Failed", {
          query: query.slice(0, 100),
          reason: "unavailable",
          page: append ? "more" : "fresh",
        });
      });
  }

  // Expose the modal so the sidebar and homepage search boxes can open it.
  window.gsOpenSearch = openSearch;

  search_open.addEventListener("click", function(event) {
    event.preventDefault();
    openSearch();
  });
  if (search_close) {
    search_close.addEventListener("click", function(event) {
      event.preventDefault();
      closeSearch();
    });
  }
  search_form.addEventListener("submit", function(event) {
    event.preventDefault();
    runSearch(false);
  });
  search_input.addEventListener("input", function() {
    clearTimeout(debounce);
    debounce = setTimeout(function() { runSearch(false); }, 220);
  });
  search_input.addEventListener("keydown", function(event) {
    if (event.key === "Escape") closeSearch();
  });
  if (search_more) {
    search_more.addEventListener("click", function(event) {
      event.preventDefault();
      runSearch(true);
    });
  }
  function onResultActivate(event) {
    // auxclick fires for every non-primary button; only the middle button
    // (button 1) opens a result in a new tab, so ignore the rest.
    if (event.type === "auxclick" && event.button !== 1) return;
    const link = event.target.closest && event.target.closest(".site-search__result-title a");
    if (!link) return;
    flushPerformed();
    track("Docs.Search.ResultClicked", {
      query: renderedQuery.slice(0, 100),
      group: link.getAttribute("data-group") || "",
      position: Number(link.getAttribute("data-pos")) || 0,
      url: link.getAttribute("href") || "",
    });
  }
  search_list.addEventListener("click", onResultActivate);
  // Middle-click (open in new tab) fires auxclick, not click, so track it too.
  search_list.addEventListener("auxclick", onResultActivate);

  // The Performed event is deferred by 1.5 s. Flush it when the page is hidden
  // or unloaded so a quick tab close or back navigation, common after a
  // zero-result search, is not lost. The helper uses keepalive to send it.
  window.addEventListener("pagehide", flushPerformed);
  document.addEventListener("visibilitychange", function() {
    if (document.visibilityState === "hidden") flushPerformed();
  });
}

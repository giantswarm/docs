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
const search_status = root.querySelector(".site-search__status");
const search_loading = root.querySelector(".site-search__loading");

if (search_open && search_form && search_input && search_list) {
  const SEARCH_ENDPOINT = "/searchapi/";
  const PAGE_SIZE = 10;
  const BLOG_SIZE = 4;
  const MAX_QUERY = 200;
  const MIN_QUERY = 2;
  // The gateway rejects a from offset above this, so stop paging before it.
  const MAX_FROM = 1000;
  // Groups in display order. Docs and release notes (Changes) come from one
  // query; blog posts come from a separate query so relevant ones always show.
  // The gateway scores blog far below docs, so in a mixed query blog would
  // never reach the top results. Handbook is not searched.
  const GROUP_ORDER = ["Docs", "Blog", "Changes"];

  let docsHits = [];
  let docsTotal = 0;
  let blogHits = [];
  let query = "";
  let controller = null;
  let debounce = null;
  // The control that opened the modal, so focus can return to it on close.
  let lastTrigger = null;
  // When paging with "More results", the index of the first new docs result,
  // so focus can move there instead of being lost. -1 means a fresh search.
  let appendFocusIndex = -1;

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

  // Allow absolute http(s) URLs and root-relative paths only. The negative
  // lookahead after the slash rejects protocol-relative URLs like //evil.example.
  function safeHref(url) {
    return /^(https?:\/\/|\/(?!\/))/.test(url) ? escapeHtml(url) : "#";
  }

  function breadcrumbText(source) {
    if (!source.breadcrumb || !source.breadcrumb.length) return "";
    return escapeHtml(source.breadcrumb.join(" › "));
  }

  // A docs-query hit is either a release note (breadcrumb "changes") or a docs page.
  function docsGroupOf(source) {
    if (source.breadcrumb && source.breadcrumb[0] === "changes") return "Changes";
    return "Docs";
  }

  function announce(message) {
    if (search_status) search_status.textContent = message || "";
  }

  function setBusy(busy) {
    search_list.setAttribute("aria-busy", busy ? "true" : "false");
    if (search_loading) search_loading.hidden = !busy;
  }

  // Keep Tab inside the open dialog. On Tab at an edge, wrap to the other end.
  function trapFocus(event) {
    if (event.key !== "Tab") return;
    const focusable = search_popup.querySelectorAll(
      'a[href], button:not([disabled]), input, [tabindex]:not([tabindex="-1"])'
    );
    const visible = Array.prototype.filter.call(focusable, function(el) {
      return !el.hidden && el.offsetParent !== null;
    });
    if (!visible.length) return;
    const first = visible[0];
    const last = visible[visible.length - 1];
    // The modal is in a shadow root, so the focused element is root.activeElement,
    // not document.activeElement (which reports the shadow host).
    const active = root.activeElement;
    if (event.shiftKey && active === first) {
      event.preventDefault();
      last.focus();
    } else if (!event.shiftKey && active === last) {
      event.preventDefault();
      first.focus();
    }
  }

  function onPopupKeydown(event) {
    if (event.key === "Escape") {
      closeSearch();
      return;
    }
    trapFocus(event);
  }

  function openSearch() {
    search_popup.classList.add("site-search__popup--active");
    document.body.classList.add("site-search-active");
    search_popup.addEventListener("keydown", onPopupKeydown);
    // Focus the input once the open animation has settled.
    window.setTimeout(function() {
      if (search_popup.classList.contains("site-search__popup--active")) {
        search_input.focus();
      }
    }, 250);
  }

  function closeSearch() {
    search_popup.classList.remove("site-search__popup--active");
    search_popup.classList.remove("site-search__popup--form-submitted");
    document.body.classList.remove("site-search-active");
    search_popup.removeEventListener("keydown", onPopupKeydown);
    // Stop any pending or in-flight search so late results can't update a hidden modal.
    clearTimeout(debounce);
    if (controller) controller.abort();
    controller = null;
    setBusy(false);
    announce("");
    // Return focus to the control that opened the modal.
    const target = lastTrigger || search_open;
    if (target && typeof target.focus === "function") target.focus();
  }

  // The whole row is one link, so a click anywhere on the result follows it.
  function renderResult(hit) {
    const source = hit._source || {};
    const highlight = hit.highlight || {};
    const title = highlight.title && highlight.title[0]
      ? withHighlight(highlight.title[0])
      : escapeHtml(source.title);
    const snippet = highlight.body && highlight.body[0]
      ? withHighlight(highlight.body[0])
      : escapeHtml(source.description || "");
    const crumb = breadcrumbText(source);
    let html = '<li class="site-search__result">';
    html += '<a class="site-search__result-link" href="' + safeHref(source.url) + '">';
    if (crumb) {
      html += '<div class="site-search__result-breadcrumb">' + crumb + "</div>";
    }
    html += '<div class="site-search__result-title">' + title + "</div>";
    if (snippet) {
      html += '<div class="site-search__result-desc">' + snippet + "</div>";
    }
    return html + "</a></li>";
  }

  function summaryText() {
    const parts = [];
    if (docsTotal) {
      parts.push(docsTotal + (docsTotal === 1 ? " documentation result" : " documentation results"));
    }
    if (blogHits.length) {
      parts.push(blogHits.length + (blogHits.length === 1 ? " blog result" : " blog results"));
    }
    return parts.join(", ");
  }

  function renderResults() {
    const groups = { Docs: [], Blog: [], Changes: [] };
    docsHits.forEach(function(hit) {
      groups[docsGroupOf(hit._source || {})].push(hit);
    });
    blogHits.forEach(function(hit) { groups.Blog.push(hit); });

    const count = docsHits.length + blogHits.length;
    const summary = summaryText();

    let html = "";
    if (summary) {
      html += '<div class="site-search__summary">' + escapeHtml(summary) + "</div>";
    }
    GROUP_ORDER.forEach(function(name) {
      const items = groups[name];
      if (items.length === 0) return;
      html += '<div class="site-search__group">';
      html += '<h2 class="site-search__group-title">' + name + " (" + items.length + ")</h2>";
      html += '<ul class="site-search__result-list" data-group="' + name + '">';
      items.forEach(function(hit) { html += renderResult(hit); });
      html += "</ul></div>";
    });

    search_list.innerHTML = html;
    setBusy(false);
    if (search_zero) search_zero.hidden = count > 0;
    if (search_error) search_error.hidden = true;
    // Hide "More results" at the end of the list or at the gateway's from-limit.
    if (search_more) {
      search_more.hidden = docsHits.length >= docsTotal || docsHits.length + PAGE_SIZE > MAX_FROM;
    }
    announce(count > 0 ? (summary || (count + " results")) : "No results");

    // After paging, move focus to the first newly loaded docs result.
    if (appendFocusIndex >= 0) {
      const list = search_list.querySelector('.site-search__result-list[data-group="Docs"]');
      const item = list && list.children[appendFocusIndex];
      const link = item && item.querySelector(".site-search__result-link");
      if (link) link.focus();
      appendFocusIndex = -1;
    }
  }

  function showFallback() {
    search_list.innerHTML = "";
    setBusy(false);
    if (search_zero) search_zero.hidden = true;
    if (search_more) search_more.hidden = true;
    const message = "Search is unavailable right now.";
    if (search_error) {
      const url = "https://www.google.com/search?q=" + encodeURIComponent("site:docs.giantswarm.io " + query);
      search_error.innerHTML = escapeHtml(message) + " "
        + '<a href="' + url + '" target="_blank" rel="noopener">Search on Google instead'
        + '<span class="site-search__sr-only"> (opens in a new tab)</span></a>.';
      search_error.hidden = false;
    }
    announce(message);
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
    }

    // Drop any in-flight request so a slower earlier query cannot render late.
    if (controller) controller.abort();
    controller = null;

    if (query.length < MIN_QUERY) {
      search_popup.classList.remove("site-search__popup--form-submitted");
      search_list.innerHTML = "";
      setBusy(false);
      announce("");
      if (search_zero) search_zero.hidden = true;
      if (search_error) search_error.hidden = true;
      if (search_more) search_more.hidden = true;
      return;
    }

    // Remember where the new docs results will start, to move focus there after paging.
    appendFocusIndex = append ? docsHits.length : -1;

    controller = typeof AbortController !== "undefined" ? new AbortController() : null;
    const signal = controller ? controller.signal : undefined;

    search_popup.classList.add("site-search__popup--form-submitted");
    setBusy(true);

    // Docs (and release notes) in one query; a smaller blog query runs only on a
    // fresh search, so "More results" pages the docs list without refetching blog.
    const docsTask = load("&type=Documentation&size=" + PAGE_SIZE + "&from=" + docsHits.length, signal)
      .then(function(data) {
        const page = (data && data.hits && data.hits.hits) || [];
        docsTotal = (data && data.hits && data.hits.total && data.hits.total.value) || 0;
        docsHits = docsHits.concat(page);
      });
    const tasks = [docsTask];
    if (!append) {
      // A failed blog query must not hide docs results, so swallow its error.
      tasks.push(
        load("&type=Blog&size=" + BLOG_SIZE, signal)
          .then(function(data) {
            blogHits = (data && data.hits && data.hits.hits) || [];
          })
          .catch(function() { blogHits = []; })
      );
    }

    Promise.allSettled(tasks).then(function(results) {
      const docsResult = results[0];
      if (docsResult.status === "rejected") {
        const reason = docsResult.reason;
        if (reason && reason.name === "AbortError") return;
        showFallback();
        return;
      }
      renderResults();
    });
  }

  // Expose the modal so the sidebar and homepage search boxes can open it. The
  // trigger is passed so focus can return to it when the modal closes.
  window.gsOpenSearch = function(trigger) {
    lastTrigger = trigger || search_open;
    openSearch();
  };

  search_open.addEventListener("click", function(event) {
    event.preventDefault();
    lastTrigger = search_open;
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
    // Cancel the pending debounce so Enter doesn't fire a second identical search.
    clearTimeout(debounce);
    runSearch(false);
  });
  search_input.addEventListener("input", function() {
    clearTimeout(debounce);
    debounce = setTimeout(function() { runSearch(false); }, 220);
  });
  if (search_more) {
    search_more.addEventListener("click", function(event) {
      event.preventDefault();
      runSearch(true);
    });
  }
}

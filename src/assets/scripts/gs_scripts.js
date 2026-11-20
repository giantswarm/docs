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
  const CHANGES_SIZE = 5;
  const MAX_QUERY = 200;
  const MIN_QUERY = 2;
  // The gateway rejects a from offset above this, so stop paging before it.
  const MAX_FROM = 1000;
  // Groups in display order. Regular documentation comes from the main query.
  // Release notes (Changes) rank far below docs in that query, so they get their
  // own query and show as a smaller group below docs. Blog and Handbook are not
  // searched.
  const GROUP_ORDER = ["Docs", "Changes"];

  let docsHits = [];
  let docsTotal = 0;
  let docsTotalGte = false;
  let changesHits = [];
  let query = "";
  let controller = null;
  let debounce = null;
  // The control that opened the modal, so focus can return to it on close.
  let lastTrigger = null;
  // When paging with "More results", the index of the first new docs result,
  // so focus can move there instead of being lost. -1 means a fresh search.
  let appendFocusIndex = -1;
  // Telemetry state. renderedQuery is the query the on-screen results belong to,
  // so a click reports it even when a newer search is already in flight.
  let renderedQuery = "";
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
      // getClientRects works for position:fixed elements; offsetParent is null for them.
      return !el.hidden && el.getClientRects().length > 0;
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
    flushPerformed();
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

  // The title is the link. A stretched ::after (see the styles) makes the whole
  // row clickable, while the screen-reader link name stays just the title.
  // group and position tag the link so a click can be reported to telemetry.
  function renderResult(hit, group, position) {
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
    if (crumb) {
      html += '<div class="site-search__result-breadcrumb">' + crumb + "</div>";
    }
    html += '<a class="site-search__result-link" href="' + safeHref(source.url) + '"'
      + ' data-group="' + escapeHtml(group) + '" data-pos="' + position + '">' + title + "</a>";
    if (snippet) {
      html += '<div class="site-search__result-desc">' + snippet + "</div>";
    }
    return html + "</li>";
  }

  function summaryText() {
    if (!docsTotal) return "";
    // The gateway caps the total at 10,000 and reports relation "gte" beyond that.
    const n = docsTotalGte ? docsTotal.toLocaleString() + "+" : docsTotal.toLocaleString();
    return n + (docsTotal === 1 ? " result" : " results");
  }

  function renderResults() {
    // The main query is documentation. Any release note it happens to return is
    // dropped here, because the Changes group comes from the dedicated query.
    const groups = { Docs: [], Changes: [] };
    docsHits.forEach(function(hit) {
      if (docsGroupOf(hit._source || {}) === "Changes") return;
      groups.Docs.push(hit);
    });
    changesHits.forEach(function(hit) { groups.Changes.push(hit); });

    const count = groups.Docs.length + groups.Changes.length;
    const summary = summaryText();

    let html = "";
    if (summary) {
      html += '<div class="site-search__summary">' + escapeHtml(summary) + "</div>";
    }
    let position = 0;
    GROUP_ORDER.forEach(function(name) {
      const items = groups[name];
      if (items.length === 0) return;
      html += '<div class="site-search__group">';
      html += '<h2 class="site-search__group-title">' + name + " (" + items.length + ")</h2>";
      html += '<ul class="site-search__result-list" data-group="' + name + '">';
      items.forEach(function(hit) { position += 1; html += renderResult(hit, name, position); });
      html += "</ul></div>";
    });

    // Remember which query these results belong to, so a click reports the query
    // that was on screen even if a newer search is already in flight.
    renderedQuery = query;
    search_list.innerHTML = html;
    setBusy(false);
    if (search_zero) search_zero.hidden = count > 0;
    if (search_error) search_error.hidden = true;
    // Hide "More results" at the end of the list or at the gateway's from-limit.
    if (search_more) {
      search_more.hidden = docsHits.length >= docsTotal || docsHits.length + PAGE_SIZE > MAX_FROM;
    }
    // Include the query so two searches with the same count still announce.
    const outcome = count > 0 ? (summary || (count + " results")) : "No results";
    announce(outcome + ' for "' + query + '"');

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
      docsTotalGte = false;
      changesHits = [];
      searchStart = Date.now();
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
      // The box was cleared or shortened below the minimum. A search that already
      // rendered (often a zero-result one the reader is about to retype) is still
      // worth recording, so flush it instead of dropping it.
      flushPerformed();
      return;
    }

    // Remember where the new docs results will start, to move focus there after
    // paging. Count only the Docs-group items, since release notes from the main
    // query are rendered in the Changes group, not the Docs list.
    appendFocusIndex = append
      ? docsHits.filter(function(h) { return docsGroupOf(h._source || {}) !== "Changes"; }).length
      : -1;

    controller = typeof AbortController !== "undefined" ? new AbortController() : null;
    const signal = controller ? controller.signal : undefined;

    search_popup.classList.add("site-search__popup--form-submitted");
    setBusy(true);

    // Documentation is the main query. "More results" pages it with a higher from
    // offset. Release notes rank far below docs in that query, so a smaller changes
    // query runs only on a fresh search and fills the Changes group.
    const docsTask = load("&type=Documentation&size=" + PAGE_SIZE + "&from=" + docsHits.length, signal)
      .then(function(data) {
        const page = (data && data.hits && data.hits.hits) || [];
        const total = (data && data.hits && data.hits.total) || {};
        docsTotal = total.value || 0;
        docsTotalGte = total.relation === "gte";
        docsHits = docsHits.concat(page);
      });
    const tasks = [docsTask];
    if (!append) {
      // A failed changes query must not hide docs results, so swallow its error.
      tasks.push(
        load("&type=Documentation&breadcrumb=changes&size=" + CHANGES_SIZE, signal)
          .then(function(data) {
            changesHits = (data && data.hits && data.hits.hits) || [];
          })
          .catch(function() { changesHits = []; })
      );
    }

    Promise.allSettled(tasks).then(function(results) {
      const docsResult = results[0];
      if (docsResult.status === "rejected") {
        const reason = docsResult.reason;
        if (reason && reason.name === "AbortError") return;
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
        return;
      }
      renderResults();
      if (!append) {
        schedulePerformed(docsHits.length + changesHits.length);
      }
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

  function onResultActivate(event) {
    // auxclick fires for every non-primary button; only the middle button
    // (button 1) opens a result in a new tab, so ignore the rest.
    if (event.type === "auxclick" && event.button !== 1) return;
    const link = event.target.closest && event.target.closest(".site-search__result-link");
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

  // The Performed event is deferred by 1.5 s. Flush it when the page is hidden or
  // unloaded so a quick tab close or back navigation, common after a zero-result
  // search, is not lost. The helper uses keepalive to send it.
  window.addEventListener("pagehide", flushPerformed);
  document.addEventListener("visibilitychange", function() {
    if (document.visibilityState === "hidden") flushPerformed();
  });
}

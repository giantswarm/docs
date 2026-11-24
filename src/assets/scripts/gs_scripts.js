// The header, the mobile drawer and the search overlay are taken from
// www.giantswarm.io and rendered in a shadow root, which none of the website's
// own scripts can reach. This is the part of their behaviour the docs site
// needs, with the lookups pointed at the shadow root.
const root = document.querySelector('#header').shadowRoot;

// The website locks the page behind its overlays with a class on the body.
// That rule sits inside the shadow root here, where it matches nothing, so the
// lock is set directly. The counter keeps the drawer and the search overlay
// from unlocking each other.
let scroll_locks = 0;
function lockScroll(locked) {
  scroll_locks = Math.max(0, scroll_locks + (locked ? 1 : -1));
  document.body.style.overflow = scroll_locks > 0 ? "hidden" : "";
}

// Navigation dropdowns. Each item carries its own button and panel, and a
// panel is shown by taking its hidden attribute away.
const nav_items = root.querySelectorAll("[data-nav-dropdown]");
const nav_open = new Set();

function navPanel(item) {
  return item.querySelector(".gs-nav__panel");
}

function navTrigger(item) {
  return item.querySelector("button[aria-expanded]");
}

function closeNavItem(item) {
  const trigger = navTrigger(item);
  const panel = navPanel(item);
  if (!trigger || !panel) return;
  trigger.setAttribute("aria-expanded", "false");
  panel.setAttribute("hidden", "");
  nav_open.delete(item);
}

function openNavItem(item) {
  const trigger = navTrigger(item);
  const panel = navPanel(item);
  if (!trigger || !panel) return;
  nav_items.forEach(function(other) {
    if (other !== item) closeNavItem(other);
  });
  trigger.setAttribute("aria-expanded", "true");
  panel.removeAttribute("hidden");
  nav_open.add(item);
}

function closeAllNavItems() {
  nav_open.forEach(closeNavItem);
}

nav_items.forEach(function(item) {
  const trigger = navTrigger(item);
  const panel = navPanel(item);
  if (!trigger || !panel) return;

  let close_timer = null;
  function scheduleClose() {
    clearTimeout(close_timer);
    close_timer = setTimeout(function() { closeNavItem(item); }, 120);
  }
  function cancelClose() {
    clearTimeout(close_timer);
  }

  item.addEventListener("mouseenter", function() {
    cancelClose();
    openNavItem(item);
  });
  item.addEventListener("mouseleave", scheduleClose);
  panel.addEventListener("mouseenter", cancelClose);
  panel.addEventListener("mouseleave", scheduleClose);
  trigger.addEventListener("click", function(event) {
    event.preventDefault();
    if (nav_open.has(item)) {
      closeNavItem(item);
    } else {
      openNavItem(item);
    }
  });
  item.addEventListener("focusin", function() {
    cancelClose();
    openNavItem(item);
  });
  item.addEventListener("focusout", function(event) {
    if (!item.contains(event.relatedTarget)) scheduleClose();
  });
});

// A click outside an item closes the panels. It takes two listeners: a click
// inside the shadow root is reported to the document as a click on the host,
// so the document alone cannot tell where it landed.
root.addEventListener("click", function(event) {
  if (!event.target.closest("[data-nav-dropdown]")) closeAllNavItems();
});
document.addEventListener("click", function(event) {
  if (event.target !== root.host) closeAllNavItems();
});
document.addEventListener("keydown", function(event) {
  if (event.key !== "Escape" || nav_open.size === 0) return;
  const last = Array.from(nav_open).pop();
  closeAllNavItems();
  if (last) navTrigger(last).focus();
});

// Mobile drawer. It holds a root view and a view per section, of which one is
// visible at a time.
const menu = root.querySelector(".gs-mobile-menu");
const menu_toggles = root.querySelectorAll("[data-menu-toggle]");

if (menu && menu_toggles.length) {
  const menu_views = menu.querySelectorAll("[data-view]");
  const menu_root_view = menu.querySelector('[data-view="root"]');

  // The website picks the drawer's colours from the header it opened under.
  // The docs header is always the solid one, which pairs with the light drawer.
  menu.classList.add("gs-mobile-menu--light");

  const showView = function(id) {
    let target = null;
    menu_views.forEach(function(view) {
      if (view.getAttribute("data-view") === id) {
        target = view;
        view.removeAttribute("hidden");
      } else {
        view.setAttribute("hidden", "");
      }
    });
    if (!target) return;
    target.scrollTop = 0;
    const back = target.querySelector("[data-menu-back]");
    if (back) back.focus();
  };

  const menuIsOpen = function() {
    return !menu.hasAttribute("hidden");
  };

  const openMenu = function() {
    if (menuIsOpen()) return;
    menu.removeAttribute("hidden");
    lockScroll(true);
    menu_toggles.forEach(function(toggle) {
      toggle.setAttribute("aria-expanded", "true");
      toggle.setAttribute("aria-label", "Close menu");
    });
  };

  const closeMenu = function() {
    if (!menuIsOpen()) return;
    menu.setAttribute("hidden", "");
    lockScroll(false);
    menu_toggles.forEach(function(toggle) {
      toggle.setAttribute("aria-expanded", "false");
      toggle.setAttribute("aria-label", "Open menu");
    });
    showView("root");
  };

  menu_toggles.forEach(function(toggle) {
    toggle.addEventListener("click", function(event) {
      event.preventDefault();
      if (menuIsOpen()) {
        closeMenu();
      } else {
        openMenu();
      }
    });
  });
  menu.querySelectorAll("[data-menu-drill]").forEach(function(button) {
    button.addEventListener("click", function() {
      const target = button.getAttribute("data-menu-drill");
      if (target) showView(target);
    });
  });
  menu.querySelectorAll("[data-menu-back]").forEach(function(button) {
    button.addEventListener("click", function() { showView("root"); });
  });
  menu.querySelectorAll("a").forEach(function(link) {
    link.addEventListener("click", function() { setTimeout(closeMenu, 0); });
  });
  document.addEventListener("keydown", function(event) {
    if (event.key !== "Escape" || !menuIsOpen()) return;
    if (menu_root_view.hasAttribute("hidden")) {
      showView("root");
    } else {
      closeMenu();
    }
  });
  window.addEventListener("resize", function() {
    if (menuIsOpen() && window.innerWidth >= 1025) closeMenu();
  });
}

// Self-hosted docs search. The modal queries the /searchapi gateway on
// docs-proxy, which takes a few validated parameters and returns only the
// fields a result needs (see docs-proxy search.js). Everything the gateway
// returns is rendered as text, never HTML, because it comes from a public
// repo that takes outside PRs and from HubSpot.
const search_popup = root.querySelector(".gs-search");
const search_input = root.querySelector(".gs-search__input");
const search_toggles = root.querySelectorAll("[data-search-toggle]");
const search_dismissers = root.querySelectorAll("[data-search-dismiss]");
const search_list = root.querySelector(".gs-search__results");
const search_intro = root.querySelector(".gs-search__intro");
const search_zero = root.querySelector(".gs-search__empty");
const search_zero_query = root.querySelector("[data-search-query]");
const search_error = root.querySelector(".gs-search__error");
const search_more = root.querySelector(".gs-search__more");
const search_status = root.querySelector(".gs-search__status");
const search_loading = root.querySelector(".gs-search__loading");

if (search_popup && search_input && search_list) {
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

  // The gateway wraps matched terms in the private-use characters U+E000 and
  // U+E001, which cannot occur in indexed content. The markers are built from
  // their code points, the way the gateway builds them, because written out
  // literally they are invisible in the source.
  const HIGHLIGHT_OPEN = String.fromCharCode(0xe000);
  const HIGHLIGHT_CLOSE = String.fromCharCode(0xe001);
  const HIGHLIGHT_PATTERN = new RegExp(
    HIGHLIGHT_OPEN + "([^" + HIGHLIGHT_CLOSE + "]+?)" + HIGHLIGHT_CLOSE, "g"
  );

  // Escape the whole string first so index content can never inject markup,
  // then turn the markers into highlight spans.
  function withHighlight(value) {
    return escapeHtml(value).replace(HIGHLIGHT_PATTERN, '<span class="hs-search-highlight">$1</span>');
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

  // Move focus from result to result. Enter then follows the focused link by
  // itself, which is what the footer of the overlay promises.
  function moveSelection(step) {
    const results = Array.prototype.slice.call(
      search_list.querySelectorAll(".gs-search__result")
    );
    if (!results.length) return;
    const current = results.indexOf(root.activeElement);
    let next = current < 0 ? (step > 0 ? 0 : results.length - 1) : current + step;
    if (next < 0) next = results.length - 1;
    if (next >= results.length) next = 0;
    results[next].focus();
  }

  function onPopupKeydown(event) {
    if (event.key === "Escape") {
      closeSearch();
      return;
    }
    if (event.key === "ArrowDown" || event.key === "ArrowUp") {
      event.preventDefault();
      moveSelection(event.key === "ArrowDown" ? 1 : -1);
      return;
    }
    trapFocus(event);
  }

  function searchIsOpen() {
    return !search_popup.hasAttribute("hidden");
  }

  function openSearch() {
    if (searchIsOpen()) return;
    search_popup.removeAttribute("hidden");
    lockScroll(true);
    search_popup.addEventListener("keydown", onPopupKeydown);
    requestAnimationFrame(function() {
      search_input.focus();
      search_input.select();
    });
  }

  function closeSearch() {
    if (!searchIsOpen()) return;
    flushPerformed();
    search_popup.setAttribute("hidden", "");
    lockScroll(false);
    search_popup.removeEventListener("keydown", onPopupKeydown);
    // Stop any pending or in-flight search so late results can't update a hidden modal.
    clearTimeout(debounce);
    if (controller) controller.abort();
    controller = null;
    setBusy(false);
    announce("");
    // Return focus to the control that opened the modal.
    const target = lastTrigger || search_toggles[0];
    if (target && typeof target.focus === "function") target.focus();
  }

  // The whole row is the link. group and position tag it so that a click can
  // be reported to telemetry.
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
    let html = '<a class="gs-search__result" href="' + safeHref(source.url) + '"'
      + ' data-group="' + escapeHtml(group) + '" data-pos="' + position + '">';
    html += '<span class="gs-search__result-head">'
      + '<span class="gs-search__result-title">' + title + "</span>"
      + '<span class="gs-search__result-type">' + escapeHtml(group) + "</span>"
      + "</span>";
    if (crumb) {
      html += '<span class="gs-search__result-breadcrumb">' + crumb + "</span>";
    }
    if (snippet) {
      html += '<span class="gs-search__result-desc">' + snippet + "</span>";
    }
    return html + "</a>";
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
      html += '<div class="gs-search__summary">' + escapeHtml(summary) + "</div>";
    }
    let position = 0;
    GROUP_ORDER.forEach(function(name) {
      const items = groups[name];
      if (items.length === 0) return;
      html += '<div class="gs-search__group" data-group="' + name + '">';
      html += '<p class="gs-search__group-title">' + name + " (" + items.length + ")</p>";
      items.forEach(function(hit) { position += 1; html += renderResult(hit, name, position); });
      html += "</div>";
    });

    // Remember which query these results belong to, so a click reports the query
    // that was on screen even if a newer search is already in flight.
    renderedQuery = query;
    search_list.innerHTML = html;
    setBusy(false);
    if (search_intro) search_intro.hidden = true;
    if (search_zero) search_zero.hidden = count > 0;
    if (search_zero_query) search_zero_query.textContent = query;
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
      const group = search_list.querySelector('.gs-search__group[data-group="Docs"]');
      const links = group ? group.querySelectorAll(".gs-search__result") : [];
      const link = links[appendFocusIndex];
      if (link) link.focus();
      appendFocusIndex = -1;
    }
  }

  function showFallback() {
    search_list.innerHTML = "";
    setBusy(false);
    if (search_intro) search_intro.hidden = true;
    if (search_zero) search_zero.hidden = true;
    if (search_more) search_more.hidden = true;
    const message = "Search is unavailable right now.";
    if (search_error) {
      const url = "https://www.google.com/search?q=" + encodeURIComponent("site:docs.giantswarm.io " + query);
      search_error.innerHTML = escapeHtml(message) + " "
        + '<a href="' + url + '" target="_blank" rel="noopener">Search on Google instead'
        + '<span class="gs-search__sr-only"> (opens in a new tab)</span></a>.';
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
      if (search_intro) search_intro.hidden = false;
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

    if (search_intro) search_intro.hidden = true;
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
    lastTrigger = trigger || search_toggles[0];
    openSearch();
  };

  search_toggles.forEach(function(toggle) {
    toggle.addEventListener("click", function(event) {
      event.preventDefault();
      lastTrigger = toggle;
      openSearch();
    });
  });
  search_dismissers.forEach(function(dismisser) {
    dismisser.addEventListener("click", function(event) {
      event.preventDefault();
      closeSearch();
    });
  });
  search_input.addEventListener("keydown", function(event) {
    if (event.key !== "Enter") return;
    event.preventDefault();
    // Cancel the pending debounce so Enter doesn't fire a second identical search.
    clearTimeout(debounce);
    runSearch(false);
  });
  // The same shortcut the website uses, and the hint that advertises it.
  document.addEventListener("keydown", function(event) {
    if (!(event.metaKey || event.ctrlKey) || event.code !== "KeyK") return;
    event.preventDefault();
    if (searchIsOpen()) {
      closeSearch();
    } else {
      openSearch();
    }
  });
  root.querySelectorAll("[data-search-shortcut]").forEach(function(hint) {
    hint.textContent = /Mac|iPod|iPhone|iPad/.test(navigator.platform) ? "\u2318K" : "Ctrl K";
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
    const link = event.target.closest && event.target.closest(".gs-search__result");
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

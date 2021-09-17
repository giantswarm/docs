var act = {
  debounce: function (t, s) {
    var i = null;
    return function () {
      var e = this,
        a = arguments;
      clearTimeout(i),
        (i = setTimeout(function () {
          t.apply(e, a);
        }, s));
    };
  },
  throttle: function (s, i, n) {
    var o, r;
    return (
      (i = i || 250),
      function () {
        var e = n || this,
          a = +new Date(),
          t = arguments;
        o && a < o + i
          ? (clearTimeout(r),
            (r = setTimeout(function () {
              (o = a), s.apply(e, t);
            }, i)))
          : ((o = a), s.apply(e, t));
      }
    );
  },
  hex: function (e) {
    return (e = e.match(
      /^rgba?[\s+]?\([\s+]?(\d+)[\s+]?,[\s+]?(\d+)[\s+]?,[\s+]?(\d+)[\s+]?/i
    )) && 4 === e.length
      ? "#" +
          ("0" + parseInt(e[1], 10).toString(16)).slice(-2) +
          ("0" + parseInt(e[2], 10).toString(16)).slice(-2) +
          ("0" + parseInt(e[3], 10).toString(16)).slice(-2)
      : "";
  },
};
jQuery(function (C) {
  C(document);
  var b,
    m,
    v,
    i,
    t,
    w = C(window),
    y = C("html, body"),
    n = C("html"),
    o = C("body");
  window.location.hash && (b = window.location.hash.replace(/^.*?(#|$)/, "")),
    o.prepend(
      '<div class="media-md"></div><div class="media-sm"></div><div class="media-xs"></div><div class="theme-color bg-theme"></div>'
    ),
    C(".media-md")
      .eq(0)
      .each(function () {
        var e = C(this),
          a = e.width();
        o.attr("data-media-md", a), (m = a), e.remove();
      }),
    C(".media-sm")
      .eq(0)
      .each(function () {
        var e = C(this),
          a = e.width();
        o.attr("data-media-sm", a), (v = a), e.remove();
      }),
    C(".media-xs")
      .eq(0)
      .each(function () {
        var e = C(this),
          a = e.width();
        o.attr("data-media-xs", a), (i = a), e.remove();
      }),
    C(".menu-bar li.hs-item-has-children").each(function () {
      var e = C(this);
      0 == e.find("ul").length && e.removeClass("hs-item-has-children");
    }),
    C(".accordion-menu .hs-menu-wrapper li.hs-item-has-children ul").each(
      function () {
        C(this).closest("li").append('<span class="expand-level"></span>');
      }
    ),
    C(
      '.accordion-menu .expand-level, .accordion-menu li:has(.expand-level) > a[href="javascript:;"]'
    ).on("click", function () {
      var e = C(this).closest("li");
      e.closest("li");
      e.hasClass("expanded")
        ? e
            .removeClass("expanded")
            .find("ul")
            .addClass("hidden")
            .find(".expanded")
            .removeClass("expanded")
        : e.addClass("expanded").find("> ul").removeClass("hidden"),
        e
          .siblings()
          .removeClass("expanded")
          .find("ul")
          .addClass("hidden")
          .find("li.expanded")
          .removeClass("expanded");
    }),
    C("[data-reveal]").each(function () {
      var e = C(this),
        a = C("#" + e.attr("data-reveal"));
      e.on("click", function () {
        return e.toggleClass("on"), a.toggleClass("on"), !1;
      });
    }),
    C("[data-slide-menu]").each(function () {
      var e = C(this),
        a = e.attr("data-slide-menu"),
        t = C('[data-slide-menu="' + a + '"]').not(this),
        s = C("#" + a),
        i = s
          .closest(".row-fluid-wrapper")
          .next(".row-fluid-wrapper")
          .find(".slide-menu-overlay");
      e.on("click", function () {
        e.toggleClass("on"),
          s.toggleClass("on"),
          t.toggleClass("on"),
          i.toggleClass("on"),
          s.hasClass("on") ? o.addClass("noscroll") : o.removeClass("noscroll"),
          C("[data-slide-menu]").not(this).not(t).removeClass("on"),
          C(".slide-menu").not(s).removeClass("on"),
          C(".slide-menu-overlay").not(i).removeClass("on");
      }),
        i.on("click", function () {
          e.removeClass("on"),
            s.removeClass("on"),
            t.removeClass("on"),
            i.removeClass("on"),
            o.removeClass("noscroll");
        });
    }),
    C('.slide-menu a[href*="#"]').on("click", function () {
      C("[data-slide-menu], .slide-menu, .slide-menu-overlay").removeClass(
        "on"
      ),
        o.removeClass("noscroll");
    }),
    C(".sticky-header").each(function () {
      var a = C(this),
        e = a.closest(".sticky-header-options"),
        t = C(e.attr("data-linked-to"));
      0 < t.length
        ? w.on(
            "load resize scroll",
            act.throttle(function () {
              var e = w.scrollTop();
              t.height() + t.offset().top < e
                ? (a.addClass("on"), t.addClass("off"))
                : (a.removeClass("on"), t.removeClass("off"));
            }, 10)
          )
        : a.addClass("on");
    }),
    C(".hs-item-has-children:not(:has(ul))").removeClass(
      "hs-item-has-children"
    );
  var f = C(".hs-menu-wrapper"),
    u = f.find("> ul > li"),
    g = (f.find("> ul > li > a"), C(C(".page-section").get().reverse())),
    x = {},
    q = [];
  f.find('a[href^="http://#"], a[href^="https://#"]').each(function () {
    var e = C(this),
      a = e.attr("href").replace("http://#", "#").replace("https://#", "#");
    e.attr("href", a);
  }),
    g.each(function () {
      var e = C(this).attr("id");
      (x[e] = f.find('> ul > li > a[href="#' + e + '"]')),
        C(this).is('[class*="active-offset-"]')
          ? (q[e] =
              parseInt(
                C(this)
                  .attr("class")
                  .match(/active-offset-\d+/)[0]
                  .replace("active-offset-", "")
              ) + 1)
          : (q[e] = 200);
    }),
    w.on(
      "load scroll resize",
      act.throttle(function () {
        var i = w.scrollTop();
        g.each(function () {
          var e = C(this),
            a = e.offset().top,
            t = e.attr("id"),
            s = x[t].closest("li");
          if (i >= a - q[t])
            return (
              s.hasClass("active") ||
                (u.removeClass("active"), s.addClass("active")),
              !1
            );
          s.removeClass("active");
        });
      }, 100)
    ),
    C(".hs-inline-edit .widget-type-raw_jinja").removeAttr("data-widget-type"),
    C(".slide-menu .control-button .close i.fa.fa-close").addClass(
      "fas fa-times"
    );
});

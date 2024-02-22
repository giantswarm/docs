var months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'];

/* Prevent disabled links from causing a page reload */
$("li.disabled a").click(function() {
  event.preventDefault();
});

/* Adjust the scroll height of anchors to compensate for the fixed navbar */
window.disableShift = false;
var shiftWindow = function() {
  if (window.disableShift) {
    window.disableShift = false;
  } else {
    scrollBy(0, -100);
  };
};
if (location.hash) {shiftWindow();}
window.addEventListener("hashchange", shiftWindow);

/**
 * Returns the value of a URL parameter
 */
function getParameterByName(name) {
  name = name.replace(/[\[]/, "\\[").replace(/[\]]/, "\\]");
  var regex = new RegExp("[\\?&]" + name + "=([^&#]*)"),
      results = regex.exec(location.search);
  return results === null ? "" : decodeURIComponent(results[1].replace(/\+/g, " "));
}

/* Initialize Inkeep widget for the Search Box */
var inkeepWidget = null;
$(function() {
  inkeepWidget = Inkeep().embed({
    componentType: "SearchBar", // required
    targetElement: document.getElementById("searchInputMobile"), // required
    properties: {
      stylesheetUrls: ["/css/inkeep.css"],
      baseSettings: {
        apiKey: "edfd9409339b80d69b5e25c6f7d1765de5f4ea23d4f711ea", // required
        integrationId: "clp8yzdn00010s601l08xlvth", // required
        organizationId: "org_glSX3NU5GkGXusqB", // required
        organizationDisplayName: "Giant Swarm",
        primaryBrandColor: "#386900"
      },
      modalSettings: {
        // optional InkeepModalSettings
      },
      searchSettings: {
        // optional InkeepSearchSettings
      },
      aiChatSettings: {
        // optional InkeepAIChatSettings
      }
    },
  });
});

$(function() {
  var disclaimerShown = document.cookie.replace(/(?:(?:^|.*;\s*)disclaimerShown\s*\=\s*([^;]*).*$)|^.*$/, "$1");
  var isVintage = window.location.pathname.startsWith("/vintage");

  if (!disclaimerShown && isVintage) {
    $('#vintage-disclaimer').show();
  }

  $('#vintage-disclaimer-button').click(function() {
      $('#vintage-disclaimer').hide();
      var date = new Date();
      date.setFullYear(date.getDay() + 1); // Cookie expires after 1 day
      document.cookie = "disclaimerShown=true;expires=" + date.toUTCString() + ";path=/";
  });
});

/** Remove TOC if empty **/
var toc = $('#TableOfContents');
if (toc.length !== 0) {
  var innerToc = toc.html();
  console.debug(innerToc);
  if (typeof innerToc === "undefined" || innerToc === "") {
    toc.remove();
    $('.toc .header').remove();
  }
}

/** Adapt username in quickstart **/
var username = getParameterByName("username");
if (typeof username !== "undefined" && username !== "") {
  $(".username").text(username);
  $(".welcome-alert").show();
  $(".helloworldlink").html('Then open your running application at <a href="http://helloworld-' + username + '.gigantic.io/" target="_blank">helloworld-' + username + '.gigantic.io</a>')
}

// make all tables bootstrappy
$("table").addClass("table");

// link headlines
// Thanks to http://ben.balter.com/2014/03/13/pages-anchor-links/!
$(function() {
  return $("h2, h3, h4, h5, h6").each(function(i, el) {
    var $el, icon, id;
    $el = $(el);
    id = $el.attr('id');
    icon = '<i class="fa fa-link"></i>';
    if (id) {
      $el.addClass("headline-with-link");
      return $el.prepend($("<a />").addClass("header-link").attr("href", "#" + id).html(icon));
    }
  });
});

/** Allow user to adapt ingress URL schema in guides **/

// prepare document
$(document).ready(function(){

  // wrap placeholder string in easily addressable span
  $('.content').contents().each(function(idx, i){
    if ($(this).html()) {
      // replace non-text nodes
      $(this).html(function(){
        if (!$(this).hasClass('placeholder-immutable')) {
          return $(this).html().replace(/\.k8s\.gigantic\.io/g, "<span class='ingressBaseDomain'>.k8s.gigantic.io</span>");
        }
      });
    } else if ($(this).text() !== "") {
      // replace text nodes
      $(this).replaceWith(function(){
        var html = $(this).text().replace(/\.k8s\.gigantic\.io/g, "<span class='ingressBaseDomain'>.k8s.gigantic.io</span>");
        return html;
      });
    }
  });

  var replaceBaseDomainPlaceholder = function(value) {
    if (value.substr(0, 1) !== '.') {
      value = '.' + value;
    }
    $('.ingressBaseDomain').text(value);
  }

  // replace placeholder on click in form
  $("#ingressBaseDomainApplyButton").click(function(evt){
    evt.preventDefault();
    // manipulate URL to allow for sharing
    var text = $('#ingressBaseDomainInput').val();
    history.pushState({}, "", "?basedomain=" + encodeURI(text));
    replaceBaseDomainPlaceholder(text);
  });

  // replace placeholder based on optional URL parameter
  var baseDomain = getParameterByName("basedomain");
  if (baseDomain != "") {
    replaceBaseDomainPlaceholder(baseDomain);
    $('#ingressBaseDomainInput').val(baseDomain);
  }

  // end of jQuery $(document).ready
});

// Add TOC sidebar behavior
window.addEventListener("load", function() {
  if (!window.GSAside) return;

  var asideSelector = ".toc-sidebar";
  if (!document.querySelector(asideSelector)) return;

  var g = new GSAside(asideSelector, ".base-content", 100);
  g.init();
});


/* Deal with clicks on nav links that do not change the current anchor link. */
$("a" ).click(function() {
  var href = this.href;
  var suffix = location.hash;
  var matchesCurrentHash = (href.indexOf(suffix, href.length - suffix.length) !== -1);
  if (location.hash && matchesCurrentHash) {
    /* Force a single 'hashchange' event to occur after the click event */
    window.disableShift = true;
    location.hash='';
  };
});

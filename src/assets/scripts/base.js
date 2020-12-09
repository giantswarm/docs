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

/**
 * Perform a search and display the result
 *
 * @param q  String     The user's search query
 */
function doSearch(q) {
  // reset search
  $(".result").empty();
  $(".searchinstructions").hide();

  var limit = 100;
  $("#qinput").val(q);
  // assemble the big query object for ElasticSearch
  var postData = {
    "from": 0,
    "size": limit,
    "sort": ["_score"],
    "_source": {
      "excludes": ["text", "breadcrumb_*"]
    },
    "query": {
      "function_score": {
        "query": {
          "simple_query_string": {
            "fields": ["title^5", "uri^5", "text"],
            "default_operator": "AND",
            "query": q
          }
        },
        "functions": [
          {
            "filter": {"term": {"breadcrumb_1": "changes"}},
            "weight": 0.1
          },
          {
            "filter": {"term": {"breadcrumb_1": "api"}},
            "weight": 0.3
          }
        ]
      }
    },
    "highlight" : {
      "fields" : {
        "body" : {
          "type": "unified",
          "number_of_fragments" : 1,
          "no_match_size": 200,
          "fragment_size" : 150
        },
        "title": {
          "type": "unified",
          "number_of_fragments" : 1
        }
      }
    },
    "suggest": {
      "phrase-suggester": {
        "text": q,
        "phrase": {
          "field": "text.trigram",
          "size": 1,
          "gram_size": 3,
          "direct_generator": [
            {
              "field": "text.trigram",
              "suggest_mode": "popular",
              "min_word_length": 3,
            }
          ],
        }
      }
    }
  };
  $.ajax("/searchapi/", {
    type: "POST",
    data: JSON.stringify(postData),
    contentType: "application/json",
    dataType: "json",
    error: function(jqXHR, textStatus, errorThrown){
      console.warn("Error in ajax call to /searchapi/:", textStatus, errorThrown);
    },
    success: function(data){
      // Display suggestions
      var hasSuggestion = false;
      if (data.suggest["phrase-suggester"] && data.suggest["phrase-suggester"].length > 0 && data.suggest["phrase-suggester"][0].options.length > 0) {
        $(".suggestion").find("a").attr("href", "./?q=" + encodeURI(data.suggest["phrase-suggester"][0].options[0].text)).text(data.suggest["phrase-suggester"][0].options[0].text);
        $(".suggestion").show();
        hasSuggestion = true;
      }

      if (!hasSuggestion) {
        $(".searchinstructions").show();
      }

      if (data.hits.total == 0) {
        // Display zero hits
        $("h1").text("No results for '" + q + "', sorry.");

        

        if (typeof ga !== 'undefined') {
          ga('send', 'event', 'search', 'zerohits', q, 0);
        }

      } else {
        // Display results
        if (data.hits.total === 1) {
          $("h1").text("1 hit for '" + q + "'");
        } else {
          $("h1").text(data.hits.total + " hits for '" + q + "'");

          if (data.hits.total > limit) {
            $('#result-is-limited').text('Showing the first '+ limit +' items only').show();
          } else {
            $('#result-is-limited').hide();
          }
        }

        $.each(data.hits.hits, function(index, hit){
          $(".result").append(renderSerpEntry(index, hit));
        });

        if (typeof ga !== 'undefined') {
          ga('send', 'event', 'search', 'hits', q, data.hits.total);
        }
      }
    }
  });
}

/**
 * Returns a jQuery DOM object for a given search result entry
 *
 * @param index  Int     Index number of this entry, starting with 0
 * @param data   Object  Result hit item as returned by elasticsearch
 */
function renderSerpEntry(index, hit) {
  d = $("<a class='item'></>").attr("href", hit._source.uri);
  if (typeof(hit.highlight) !== "undefined" && typeof(hit.highlight.title) !== "undefined") {
    d.append($("<h4></h4>").html((index + 1) + ". " + hit.highlight.title));
  } else {
    d.append($("<h4></h4>").html((index + 1) + ". " + hit._source.title));
  }
  if (typeof(hit._source.breadcrumb) !== "undefined" && hit._source.breadcrumb.length > 0) {
    d.append($("<p class='sbreadcrumb'></p>").html("/" + hit._source.breadcrumb.join("/") + "/"));
  }
  if (typeof(hit.highlight) !== "undefined" && typeof(hit.highlight.body) !== "undefined" && hit.highlight.body.length > 0) {
    d.append($("<p class='snippet'></p>").html(hit.highlight.body.join(' <span class="hellip">[...]</span> ')));
  }
  return d;
}

/* handle search */
$(document).ready(function(){

  // click handler for search button
  $("#searchsubmit").click(function(evt){
    evt.preventDefault();
    $("form.search").submit();
  });

  if (document.location.pathname !== "/search/") {
    return;
  }

  var q = getParameterByName("q");

  // sanitize query string by eleminating trailing / (PHP SimpleHTTPServer problem)
  if (q.substr(q.length - 1) === "/") {
    q = q.slice(0, -1);
  }

  if (typeof(q) === "undefined" || q == null || q === "") {
    $(".feedback").hide();
    return;
  }
  doSearch(q);
});

/** Re-format the table of contents **/

var toc = $('#TableOfContents');
if (toc.length !== 0) {
  var innerToc = toc.find("ul:first-child > li:first-child > ul").html();
  if (typeof innerToc !== "undefined") {
    toc.html("<ul>" + innerToc + "</ul>");
  } else {
    $('#TableOfContents').remove();
  }
}

/** Adapt username in quickstart **/
var username = getParameterByName("username");
if (typeof username !== "undefined" && username !== "") {
  $(".username").text(username);
  $(".welcome-alert").show();
  $(".helloworldlink").html('Then open your running application at <a href="http://helloworld-' + username + '.gigantic.io/" target="_blank">helloworld-' + username + '.gigantic.io</a>')
}

/** Adapt docs menu **/
if (document.location.pathname == "/") {
  $("#homelink").addClass("active");
} else {
  $(".docsnav .nav li").each(function(index, item){
    var link = $(item).find("a").attr("href");
    if (link !== "/" && document.location.pathname.indexOf(link) == 0) {
      $(item).addClass("active");
      return;
    }
  });
}

// make all tables bootstrappy
$("table").addClass("table");

$(".search-cta input").on("change keypress keyup", function(evt){
  if ($(".search-cta input").val() === "") {
    $(".search-cta button").animate({"opacity": 0.0});
  } else {
    $(".search-cta button").animate({"opacity": 1.0});
  }
});

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

// Add TOC sidebar behaviour
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
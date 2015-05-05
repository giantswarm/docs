
hljs.initHighlightingOnLoad();

/* Scrollspy */
//var navHeight = $('#TableOfContents').outerHeight(true) + 10

/*
$('body').scrollspy({
    target: '.toc-sidebar',
    offset: navHeight
});
*/


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
        /* If we're at the bottom of the page, don't erronously scroll up */
        var scrolledToBottomOfPage = (
            (window.innerHeight + window.scrollY) >= document.body.offsetHeight
        );
        if (!scrolledToBottomOfPage) {
            scrollBy(0, -60);
        };
    };
};
if (location.hash) {shiftWindow();}
window.addEventListener("hashchange", shiftWindow);


/* Deal with clicks on nav links that do not change the current anchor link. */
$("ul.nav a" ).click(function() {
    var href = this.href;
    var suffix = location.hash;
    var matchesCurrentHash = (href.indexOf(suffix, href.length - suffix.length) !== -1);
    if (location.hash && matchesCurrentHash) {
        /* Force a single 'hashchange' event to occur after the click event */
        window.disableShift = true;
        location.hash='';
    };
});

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
    //console.debug("Searched for", q);
    $("#qinput").val(q);
    // assemble the big query object for ElasticSearch
    var postData = {
        "from": 0,
        "size": 1000,
        "sort": [{"_score": "desc"}],
        "_source": false,
        "fields": ["uri", "title", "breadcrumb", "breadcrumb_1"],
        "query": {
            "query_string": {
                "default_field": "text",
                "default_operator": "AND",
                "query": q
            }
        },
        "highlight" : {
            "fields" : {
                "body" : {
                    "fragment_size" : 150,
                    "number_of_fragments" : 3,
                    "no_match_size": 200
                },
                "title": {
                    "number_of_fragments" : 0
                }
            }
        }
    };
    $.ajax("/api/search/", {
        type: "POST",
        data: JSON.stringify(postData),
        contentType: "application/json",
        dataType: "json",
        error: function(jqXHR, textStatus, errorThrown){
            console.warn("Error in ajax call to /api/search/:", textStatus, errorThrown);
        },
        success: function(data){
            $(".result").empty();
            if (data.hits.total == 0) {
                // no results
                $("h1").text("No results for '" + q + "', sorry.");
                $("#searchinstructions").show();
                ga('send', 'event', 'search', 'zerohits', q, 0);
            } else {
                $("#searchinstructions").hide();
                if (data.hits.total === 1) {
                    $("h1").text("1 hit for '" + q + "'");
                } else {
                    $("h1").text(data.hits.total + " hits for '" + q + "'");
                }
                $.each(data.hits.hits, function(index, hit){
                    $(".result").append(renderSerpEntry(index, hit));
                });
                ga('send', 'event', 'search', 'hits', q, data.hits.total);
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
    d = $("<a class='item'></>").attr("href", hit.fields.uri);
    if (typeof(hit.highlight) !== "undefined" && typeof(hit.highlight.title) !== "undefined") {
        d.append($("<h4></h4>").html((index + 1) + ". " + hit.highlight.title));
    } else {
        d.append($("<h4></h4>").html((index + 1) + ". " + hit.fields.title));
    }
    if (typeof(hit.fields.breadcrumb) !== "undefined" && hit.fields.breadcrumb.length > 0) {
        d.append($("<p class='sbreadcrumb'></p>").html("/" + hit.fields.breadcrumb.join("/") + "/"));
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

    if (typeof(q) === "undefined" || q == null || q === "") {
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
    

/* Prettyify */
$( document ).ready(function() {
    prettyPrint();
});


/* Scrollspy */
var navHeight = $('.navbar').outerHeight(true) + 10

$('body').scrollspy({
    target: '.bs-sidebar',
    offset: navHeight
})


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

function doSearch(q) {
    console.debug("Searched for", q);
    // insert into form
    $("#qinput").val(q);
    $("h1").text("Search results for '" + q + "'");
    var postData = {
        "from": 0,
        "size": 1000,
        "sort": [{"_score": "desc"}],
        "_source": false,
        "fields": ["uri", "title", "breadcrumb", "breadcrumb_1"],
        "query": {
            //"term": {
            //    "text": q
            //}
            "multi_match": {
                "query": q,
                "fields": ["title", "text", "uri", "breadcrumb"]
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
            console.debug(data);
            $(".result").empty();
            if (data.hits.total == 0) {
                // no results
                $("h1").text("No results for '" + q + "', sorry.");
            } else {
                $("h1").text(data.hits.total + " hits for '" + q + "'");
                $.each(data.hits.hits, function(index, hit){
                    d = $("<a class='item'></>").attr("href", hit.fields.uri);
                    if (typeof(hit.highlight) !== "undefined" && typeof(hit.highlight.title) !== "undefined") {
                        d.append("<h4>" + (index + 1) + ". " + hit.highlight.title + "</h4>");
                    } else {
                        d.append("<h4>" + (index + 1) + ". " + hit.fields.title + "</h4>");
                    }
                    if (typeof(hit.highlight) !== "undefined" && typeof(hit.highlight.body) !== "undefined" && hit.highlight.body.length > 0) {
                        d.append("<p class='snippet'>" + hit.highlight.body.join(' <span class="hellip">[...]</span> ') + "</p>");
                    }
                    //d.append("<p class='uri'>" + hit.fields.uri + "</p>");
                    $(".result").append(d);
                });
            }
        }
    });
}

/* handle search */
$(document).ready(function(){
    if (document.location.pathname !== "/search/") {
        return;
    }

    // empty left sidebar
    $(".bs-sidebar").empty();
    $(".bs-sidebar").append("<div class='searchhint'>Here we could place some search filters or some hints on advanced search features.</div>");

    var q = getParameterByName("q");

    // sanitize query string by eleminating trailing / (PHP SimpleHTTPServer problem)
    if (q.substr(q.length - 1) === "/") {
        q = q.slice(0, -1);
    }

    if (typeof(q) === "undefined" || q == null || q === "") {
        return;
    }
    doSearch(q);
});

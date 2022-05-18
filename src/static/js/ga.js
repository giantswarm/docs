// Name of the cookie placed as a result of the Hubspot GDPR banner consent/declien
var cookieName = "__hs_opt_out";

// Cookie value representing that the user has given consent.
var cookieConsentValue = "no"

/* https://github.com/madmurphy/cookies.js (GPL3) Revision 8 */
!function(){function e(e,o,t,n,r,s,i){var c="";if(t)switch(t.constructor){case Number:c=t===1/0?"; expires=Fri, 31 Dec 9999 23:59:59 GMT":"; max-age="+t;break;case String:c="; expires="+t;break;case Date:c="; expires="+t.toUTCString()}return encodeURIComponent(e)+"="+encodeURIComponent(o)+c+(r?"; domain="+r:"")+(n?"; path="+n:"")+(s?"; secure":"")+(i&&"no_restriction"!==i.toString().toLowerCase()?"lax"===i.toString().toLowerCase()||1===Math.ceil(i)||!0===i?"; samesite=lax":"none"===i.toString().toLowerCase()||i<0?"; samesite=none":"; samesite=strict":"")}var o=/[\-\.\+\*]/g,t=/^(?:expires|max\-age|path|domain|secure|samesite|httponly)$/i;window.docCookies={getItem:function(e){return e&&decodeURIComponent(document.cookie.replace(new RegExp("(?:(?:^|.*;)\\s*"+encodeURIComponent(e).replace(o,"\\$&")+"\\s*\\=\\s*([^;]*).*$)|^.*$"),"$1"))||null},setItem:function(o,n,r,s,i,c,a){return!(!o||t.test(o))&&(document.cookie=e(o,n,r,s,i,c,a),!0)},removeItem:function(o,t,n,r,s){return!!this.hasItem(o)&&(document.cookie=e(o,"","Thu, 01 Jan 1970 00:00:00 GMT",t,n,r,s),!0)},hasItem:function(e){return!(!e||t.test(e))&&new RegExp("(?:^|;\\s*)"+encodeURIComponent(e).replace(o,"\\$&")+"\\s*\\=").test(document.cookie)},keys:function(){for(var e=document.cookie.replace(/((?:^|\s*;)[^\=]+)(?=;|$)|^\s*|\s*(?:\=[^;]*)?(?:\1|$)/g,"").split(/\s*(?:\=[^;]*)?;\s*/),o=e.length,t=0;t<o;t++)e[t]=decodeURIComponent(e[t]);return e},clear:function(e,o,t,n){for(var r=this.keys(),s=r.length,i=0;i<s;i++)this.removeItem(r[i],e,o,t,n)}}}(),"undefined"!=typeof module&&void 0!==module.exports&&(module.exports=docCookies);

/**
 * Add tracking to the page, if user has given consent.
 */
function addTracking() {
  // Exit early if consent declined.
  var cookie = docCookies.getItem(cookieName);
  if (!(typeof cookie === "string" && cookie == cookieConsentValue)) {
    return
  }

  $('body').append('<script async src="https://www.googletagmanager.com/gtag/js?id=G-6NLYTLFQR2"></script>');

  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());
  gtag('config', 'G-6NLYTLFQR2', {'anonymize_ip': true});
}

$(document).ready(function() {
  addTracking();
});

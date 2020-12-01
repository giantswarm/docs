// This recreates the behaviour of the Giant Swarm menu without copying over all
// of that site's javascript.

var headerLinks = document.getElementsByClassName("hs-menu-depth-1");
for (var i = 0; i < headerLinks.length; i++) {
  headerLinks[i].addEventListener('click', toggleMenu, false);
}

function toggleMenu(e) {
  e.preventDefault();

  e.currentTarget.classList.toggle("menu-expanded")

  var wrapperContainer = e.currentTarget.getElementsByClassName('hs-menu-children-wrapper-container')[0]

  if (wrapperContainer.style.display === "none" || ! wrapperContainer.style.display) {
    closeAllMenus();
    wrapperContainer.style.display = "block";
  } else {
    wrapperContainer.style.display = "none";
  }
}

function closeAllMenus() {
  for (var i = 0; i < headerLinks.length; i++) {
    var wrapperContainer = headerLinks[i].getElementsByClassName('hs-menu-children-wrapper-container')[0];

    if (wrapperContainer) {
      wrapperContainer.style.display = "none";
    }
  }
}

// Recreate open/close behaviour of the mobile menu.
var mobileMenuTrigger = document.querySelector('.menu-trigger__container');
var mobileMenu = document.querySelector('.mobile-menu');
mobileMenuTrigger.addEventListener('click', function() {
  mobileMenuTrigger.classList.toggle('open');
  mobileMenu.classList.toggle('open');
});

function clickHandler(link) {
  var l = link;
  return (e) => {
    e.preventDefault();
    var ex = l.getAttribute('aria-expanded');
    if (ex === 'true') {
      l.setAttribute('aria-expanded', 'false')
    } else {
      l.setAttribute('aria-expanded', 'true')
    }

    var itemContainer = l.nextElementSibling.querySelector('.hs-menu-children-wrapper');
    if (itemContainer.style.display === 'none') {
      itemContainer.style.display = 'block';
    } else {
      itemContainer.style.display = 'none';
    }
  }
}

// Recreate open/close behaviour of individual menu items in the mobile menu.
var mobileMenuLinks = document.querySelectorAll('.mobile-menu .hs-menu-depth-1 > a');
for (var i = 0; i < mobileMenuLinks.length; i++) {
  var link = mobileMenuLinks[i];

  link.addEventListener('click', clickHandler(link));
}
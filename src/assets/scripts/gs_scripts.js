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

// inkeep site search
const site_search_element = root.querySelector(".site-search__open");
if (site_search_element) {
  site_search_element.addEventListener("click", function(event) {
    event.preventDefault();
    window.inkeepWidget.render({
      ...window.inkeepConfig,
      isOpen: true,
    });
  });
}

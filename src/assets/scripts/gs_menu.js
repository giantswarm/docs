// This recreates the behaviour of the Giant Swarm menu without copying over all
// of that site's javascript.

const headerLinks = document.getElementsByClassName("hs-menu-depth-1");
for (let i = 0; i < headerLinks.length; i++) {
  headerLinks[i].addEventListener('click', toggleMenu, false);
}

function toggleMenu(e) {
  e.preventDefault();

  e.currentTarget.classList.toggle("menu-expanded")

  const wrapperContainer = e.currentTarget.getElementsByClassName('hs-menu-children-wrapper-container')[0]

  if (wrapperContainer.style.display === "none" || ! wrapperContainer.style.display) {
    closeAllMenus();
    wrapperContainer.style.display = "block";
  } else {
    wrapperContainer.style.display = "none";
  }
}

function closeAllMenus() {
  for (let i = 0; i < headerLinks.length; i++) {
    let wrapperContainer = headerLinks[i].getElementsByClassName('hs-menu-children-wrapper-container')[0];

    if (wrapperContainer) {
      wrapperContainer.style.display = "none";
    }
  }
}
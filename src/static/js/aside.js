(function() {
  function GSAside(asideSelector, contentSelector, topOffset) {
    if (!asideSelector || !contentSelector) {
      throw new Error('Both selectors cannot be null.');
    }

    this.selectors = {
      aside: asideSelector,
      content: contentSelector,
      mainList: 'nav > ul',
    };

    this.elements = {
      aside: null,
      asideChild: null,
      content: null,
      links: [],
      headers: [],
    };

    this.topOffset = topOffset || 0;
    this.observer = null;
    this.activeLink = null;
    this.activeClassName = 'active';
    this.numLevelsToTrack = 2;
  }

  GSAside.prototype.throttle = function(func, limit) {
    var inThrottle;
    return function() {
      var args = arguments;
      var context = this;
      if (!inThrottle) {
        func.apply(context, args);
        inThrottle = true;
        setTimeout(() => inThrottle = false, limit);
      }
    };
  };

  GSAside.prototype.init = function() {
    this.elements.aside = document.querySelector(this.selectors.aside);
    if (!this.elements.aside) {
      throw new Error(
          'The aside with selector \'' + this.selectors.aside +
          '\' could not be found!');
    }

    var asideChildren = this.elements.aside.children;
    if (asideChildren.length < 1) {
      throw new Error('The provided aside element has no children.');
    }
    this.elements.asideChild = asideChildren[0];
    this.elements.asideChild.style.position = 'sticky';
    this.elements.asideChild.style.top = this.topOffset + 'px';

    this.elements.content = document.querySelector(this.selectors.content);
    if (!this.elements.content) {
      throw new Error(
          'The content section with selector \'' + this.selectors.content +
          '\' could not be found!');
    }

    this.updateAsideHeight();
    this.gatherLinksAndHeaders();
    this.registerEventListeners();
    this.registerScrollObserver();
  };

  GSAside.prototype.updateAsideHeight = function() {
    var targetHeight = this.elements.content.scrollHeight;
    this.elements.aside.style.height = targetHeight + 'px';
  };

  GSAside.prototype.registerEventListeners = function() {
    var updateAsideHeight = this.throttle(this.updateAsideHeight.bind(this),
        150);
    window.addEventListener('resize', updateAsideHeight);
  };

  GSAside.prototype.generateLinksSelector = function() {
    var selector = '';
    for (i = 0; i < this.numLevelsToTrack; i++) {
      var currentSelector = this.selectors.mainList;

      for (var j = 0; j < i; j++) {
        currentSelector += ' ';
        currentSelector += '> li > ul';
      }

      currentSelector += ' ';
      currentSelector += '> li > a';

      if (selector.length > 0) {
        selector += ', ';
      }

      selector += currentSelector;
    }

    return selector;
  };

  GSAside.prototype.gatherLinksAndHeaders = function() {
    var i = 0;
    var selector = this.generateLinksSelector();

    this.elements.links = [].slice.call(
        this.elements.asideChild.querySelectorAll(selector), 0);

    this.elements.headers = new Array(this.elements.links.length);

    for (i = 0; i < this.elements.links.length; i++) {
      var selector = this.elements.links[i].href.split('#')[1];
      this.elements.headers[i] = document.getElementById(selector);
    }
  };

  GSAside.prototype.registerScrollObserver = function() {
    var options = {
      rootMargin: '0px 0px -90%',
      threshold: 0.5,
    };

    this.observer = new IntersectionObserver(
        this.handleScrollObserver.bind(this),
        options);

    for (var i = 0; i < this.elements.headers.length; i++) {
      var heading = this.elements.headers[i];
      if (!heading) continue;

      this.observer.observe(heading);
    }
  };

  GSAside.prototype.handleScrollObserver = function(entries) {
    var visibleEntries = [];

    for (var i = 0; i < entries.length; i++) {
      var entry = entries[i];
      var href = '#' + entry.target.getAttribute('id');

      var correspondingLink = null;
      for (var j = 0; j < this.elements.links.length; j++) {
        var link = this.elements.links[j];
        if (link.href.indexOf(href) > -1) {
          correspondingLink = link;

          break;
        }
      }

      if (entry.isIntersecting) {
        visibleEntries.push(correspondingLink);
      }
    }

    this.activateLinks(visibleEntries);
  };

  GSAside.prototype.activateLinks = function(links) {
    var selectedLink = null;
    if (links.length > 0) {
      selectedLink = links[links.length - 1];
    }

    for (var j = 0; j < this.elements.links.length; j++) {
      var currentLink = this.elements.links[j];

      if (currentLink === this.activeLink) continue;

      currentLink.classList.remove(this.activeClassName);
    }

    if (selectedLink) {
      if (this.activeLink) {
        this.activeLink.classList.remove(this.activeClassName);
      }
      selectedLink.classList.add(this.activeClassName);
      this.activeLink = selectedLink;
    }
  };

  window.GSAside = GSAside;
})();

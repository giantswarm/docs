function GSAside(asideSelector, contentSelector, topOffset) {
  if (!asideSelector || !contentSelector) {
    throw new Error('Both selectors cannot be null.');
  }

  this.selectors = {
    aside: asideSelector,
    content: contentSelector,
  };

  this.elements = {
    aside: null,
    asideChild: null,
    content: null,
    links: [],
    headers: [],
  };

  this.topOffset = topOffset || 0;
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
};

GSAside.prototype.updateAsideHeight = function() {
  var targetHeight = this.elements.content.clientHeight;
  this.elements.aside.style.height = targetHeight + 'px';
};

GSAside.prototype.registerEventListeners = function() {
  var updateAsideHeight = this.throttle(this.updateAsideHeight.bind(this), 150);
  window.addEventListener('resize', updateAsideHeight);
};

GSAside.prototype.gatherLinksAndHeaders = function() {
  this.elements.links = [].slice.call(this.elements.asideChild.querySelectorAll('a'), 0);

  this.elements.headers = new Array(this.elements.links.length);

  var selector = '';
  for (var i = 0; i < this.elements.links.length; i++) {
    selector = this.elements.links[i].href.split('#')[1];
    this.elements.headers[i] = document.getElementById(selector);
  }
};

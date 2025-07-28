/**
 * Accessible accordion navigation menu
 * Provides keyboard navigation and proper ARIA state management
 */
(function() {
  'use strict';

  class AccordionMenu {
    constructor(selector) {
      this.menu = document.querySelector(selector);
      if (!this.menu) return;

      this.toggleButtons = this.menu.querySelectorAll('.acnav__toggle');
      this.links = this.menu.querySelectorAll('.acnav__link');
      this.submenuItems = this.menu.querySelectorAll('.acnav__list--level2, .acnav__list--level3, .acnav__list--level4');

      this.init();
    }

    init() {
      this.bindEvents();
      this.setInitialStates();
    }

    bindEvents() {
      // Handle toggle button clicks
      this.toggleButtons.forEach(button => {
        button.addEventListener('click', (e) => {
          e.preventDefault();
          this.toggleSubmenu(button);
        });

        // Handle keyboard navigation
        button.addEventListener('keydown', (e) => {
          this.handleKeyDown(e, button);
        });
      });

      // Handle direct link clicks in toggle buttons
      this.toggleButtons.forEach(button => {
        const link = button.querySelector('.acnav__link');
        if (link) {
          link.addEventListener('click', (e) => {
            // Allow the link to navigate normally
            e.stopPropagation();
          });
        }
      });

      // Handle keyboard navigation for regular links
      this.links.forEach(link => {
        link.addEventListener('keydown', (e) => {
          this.handleKeyDown(e, link);
        });
      });
    }

    setInitialStates() {
      // Ensure collapsed submenus are properly hidden
      this.submenuItems.forEach(submenu => {
        const parentItem = submenu.closest('.acnav__item');
        const toggle = parentItem?.querySelector('.acnav__toggle');

        if (toggle && toggle.getAttribute('aria-expanded') === 'false') {
          submenu.style.display = 'none';
        }
      });
    }

    toggleSubmenu(button) {
      const isExpanded = button.getAttribute('aria-expanded') === 'true';
      const submenuId = button.getAttribute('aria-controls');
      const submenu = document.getElementById(submenuId);
      const parentItem = button.closest('.acnav__item');

      if (!submenu) return;

      // Update ARIA states
      button.setAttribute('aria-expanded', !isExpanded);
      button.setAttribute('aria-label',
        !isExpanded ?
        `Collapse ${this.getButtonText(button)} submenu` :
        `Expand ${this.getButtonText(button)} submenu`
      );

      // Update visual states
      if (!isExpanded) {
        // Expanding
        parentItem.classList.add('is-expanded');
        submenu.removeAttribute('aria-hidden');
        submenu.style.display = 'block';

        // Animate the expansion
        this.animateExpand(submenu);
      } else {
        // Collapsing
        parentItem.classList.remove('is-expanded');
        submenu.setAttribute('aria-hidden', 'true');

        // Animate the collapse
        this.animateCollapse(submenu);
      }

      // Close sibling submenus at the same level
      this.closeSiblingSubmenus(button);
    }

    animateExpand(submenu) {
      submenu.style.overflow = 'hidden';
      submenu.style.height = '0px';
      submenu.style.opacity = '0';

      // Force reflow
      submenu.offsetHeight;

      submenu.style.transition = 'height 0.3s ease-out, opacity 0.2s ease-out';
      submenu.style.height = submenu.scrollHeight + 'px';
      submenu.style.opacity = '1';

      // Clean up after animation
      setTimeout(() => {
        submenu.style.height = 'auto';
        submenu.style.overflow = 'visible';
        submenu.style.transition = '';
      }, 300);
    }

    animateCollapse(submenu) {
      submenu.style.overflow = 'hidden';
      submenu.style.height = submenu.scrollHeight + 'px';

      // Force reflow
      submenu.offsetHeight;

      submenu.style.transition = 'height 0.2s ease-in, opacity 0.2s ease-in';
      submenu.style.height = '0px';
      submenu.style.opacity = '0';

      // Hide after animation
      setTimeout(() => {
        submenu.style.display = 'none';
        submenu.style.height = '';
        submenu.style.opacity = '';
        submenu.style.overflow = '';
        submenu.style.transition = '';
      }, 200);
    }

    closeSiblingSubmenus(currentButton) {
      const currentLevel = this.getMenuLevel(currentButton);
      const parentList = currentButton.closest('.acnav__list');

      if (!parentList) return;

      // Find all toggle buttons at the same level
      const siblingButtons = parentList.querySelectorAll(':scope > .acnav__item > .acnav__toggle');

      siblingButtons.forEach(button => {
        if (button !== currentButton && button.getAttribute('aria-expanded') === 'true') {
          this.toggleSubmenu(button);
        }
      });
    }

    getMenuLevel(element) {
      const levelClasses = ['level1', 'level2', 'level3', 'level4'];
      const parentList = element.closest('.acnav__list');

      for (let i = 0; i < levelClasses.length; i++) {
        if (parentList && parentList.classList.contains(`acnav__list--${levelClasses[i]}`)) {
          return i + 1;
        }
      }
      return 1;
    }

    getButtonText(button) {
      const link = button.querySelector('.acnav__link');
      return link ? link.textContent.trim() : '';
    }

    handleKeyDown(e, element) {
      const key = e.key;
      const isToggleButton = element.classList.contains('acnav__toggle');

      switch (key) {
        case 'Enter':
        case ' ': // Space
          if (isToggleButton) {
            e.preventDefault();
            this.toggleSubmenu(element);
          }
          break;

        case 'ArrowDown':
          e.preventDefault();
          this.focusNext(element);
          break;

        case 'ArrowUp':
          e.preventDefault();
          this.focusPrevious(element);
          break;

        case 'ArrowRight':
          if (isToggleButton && element.getAttribute('aria-expanded') === 'false') {
            e.preventDefault();
            this.toggleSubmenu(element);
          }
          break;

        case 'ArrowLeft':
          if (isToggleButton && element.getAttribute('aria-expanded') === 'true') {
            e.preventDefault();
            this.toggleSubmenu(element);
          } else {
            // Move to parent level
            this.focusParent(element);
          }
          break;

        case 'Home':
          e.preventDefault();
          this.focusFirst();
          break;

        case 'End':
          e.preventDefault();
          this.focusLast();
          break;
      }
    }

    getAllFocusableElements() {
      return Array.from(this.menu.querySelectorAll('.acnav__toggle, .acnav__link:not(.acnav__toggle .acnav__link)'))
        .filter(el => this.isVisible(el));
    }

    isVisible(element) {
      const parentSubmenu = element.closest('.acnav__list--level2, .acnav__list--level3, .acnav__list--level4');
      if (!parentSubmenu) return true;

      return parentSubmenu.getAttribute('aria-hidden') !== 'true' &&
             getComputedStyle(parentSubmenu).display !== 'none';
    }

    focusNext(currentElement) {
      const focusableElements = this.getAllFocusableElements();
      const currentIndex = focusableElements.indexOf(currentElement);
      const nextIndex = (currentIndex + 1) % focusableElements.length;
      focusableElements[nextIndex].focus();
    }

    focusPrevious(currentElement) {
      const focusableElements = this.getAllFocusableElements();
      const currentIndex = focusableElements.indexOf(currentElement);
      const previousIndex = currentIndex === 0 ? focusableElements.length - 1 : currentIndex - 1;
      focusableElements[previousIndex].focus();
    }

    focusParent(element) {
      const parentItem = element.closest('.acnav__item').parentElement.closest('.acnav__item');
      if (parentItem) {
        const parentToggle = parentItem.querySelector('.acnav__toggle');
        const parentLink = parentItem.querySelector('.acnav__link:not(.acnav__toggle .acnav__link)');
        (parentToggle || parentLink)?.focus();
      }
    }

    focusFirst() {
      const focusableElements = this.getAllFocusableElements();
      if (focusableElements.length > 0) {
        focusableElements[0].focus();
      }
    }

    focusLast() {
      const focusableElements = this.getAllFocusableElements();
      if (focusableElements.length > 0) {
        focusableElements[focusableElements.length - 1].focus();
      }
    }
  }

  // Initialize when DOM is ready
  document.addEventListener('DOMContentLoaded', () => {
    new AccordionMenu('.acnav');
  });

  // Also initialize immediately if DOM is already loaded
  if (document.readyState === 'loading') {
    // DOMContentLoaded has not fired yet
  } else {
    // DOMContentLoaded has already fired
    new AccordionMenu('.acnav');
  }

})();
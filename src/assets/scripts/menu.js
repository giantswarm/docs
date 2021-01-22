
// Multi-level accordion nav
$('.acnav__label').click(function () {
	var label = $(this);
	var parent = label.parent('.has-children');
	var list = label.siblings('.acnav__list');

	if ( parent.hasClass('is-open') ) {
		list.slideUp('fast');
		parent.removeClass('is-open');
	}
	else {
		list.slideDown('fast');
		parent.addClass('is-open');
	}
});


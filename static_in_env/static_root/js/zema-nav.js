function zemanav() {
	if (!$('.zema-nav').hasClass('active')){
		$('.zema-nav').addClass('active');
		$('.zema-nav-trigger').addClass('is-active');
	}
	else {
		$('.zema-nav').removeClass('active')
		$('.zema-nav-trigger').removeClass('is-active')
	}
}

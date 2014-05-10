if (!window.xgfone) window.xgfone = {};
xgfone.$ = jQuery;
xgfone.scroll = function () {
	var top;
	if (document.all) top = document.documentElement.scrollTop;
	else top = window.pageYOffset
	if (top < 300) document.getElementById("back-to-top").style.visibility = "hidden";
	else document.getElementById("back-to-top").style.visibility = "visible";
}

xgfone.goTop = function () {
	window.scrollTo(0, 0);
}

xgfone.back_to_top = function () {
	if (document.all)
		window.attachEvent("onscroll", xgfone.scroll);
	else
		window.addEventListener("scroll", function () {
			xgfone.scroll();
		}, true);

	xgfone.$("#back-to-top").click(function (event) {
		xgfone.goTop();
	});
}

xgfone.menu_mouser_event = function () {
	var over_background_value = "rgba(0,50,255, 0.3)";
	var out_background_value = "rgba(255,255,255, 0.3)";
	var header_nav = xgfone.$(".header .menu ul .header-nav");
	header_nav.mouseover(function (event) {
		xgfone.$(this).css("background", over_background_value);
	});
	header_nav.mouseout(function (event) {
		xgfone.$(this).css("background", out_background_value);
	});
}
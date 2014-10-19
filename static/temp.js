
function init() {
	var len = document.getElementsByTagName('p')[0].innerHTML.length * 5;
	len = len + 'px';
	console.log(len);
	$(document).getElementById("marquee").css('min-width', len);
}
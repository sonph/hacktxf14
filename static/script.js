
/* updates real-time */
var source = new EventSource('');
source.onmessage = function(event) {
	$(document).getElementById('marquee').innerHTML = event.data;
}

/* start timer and animation */
var timer;
function init() {
	timer = setTimeout(update, 3000);	// update every 3 seconds
}

/* on stop app */
function onStop() {
	if (timer != null) {
		window.clearTimeout(timer);
	}
}

/* updates */
function update() {
	$(document).get("url", function(data, status) {
		if (status === 'success') {
			$(document).getElementById('marquee').innerHTML = data;
		}
	});
}
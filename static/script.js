
/* updates real-time */
var source = new EventSource('');
source.onmessage = function(event) {
	$(document).getElementById('marquee').innerHTML = event.data;
}

var marqueeE;

/* start timer and animation */
var timer;
function init() {
	marqueeE = $(document).getElementById('marquee');
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
			marqueeE.innerHTML = '';	// flush

			// append

			marqueeE.css('min-width',  + 'px');
		}
	});
}

/* stock price increases */
function up(company, price) {
	marqueeE.innerHTML += '<p class="up">' + company + ' ' + price + '</p>';
}
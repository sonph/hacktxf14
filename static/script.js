
var timer;

function init() {
	timer = setTimeout(update, 1000);
}

/* updates stock prices through get request */
function update() {
	var xmlHttp = null;
    xmlHttp = new XMLHttpRequest();
    xmlHttp.open( "GET", 'http://192.168.1.108:8080/api', false );
    xmlHttp.send( null );
    var response = JSON.parse(xmlHttp.responseText);

	var arr = [];
	// console.log(response['update']);
	if (response['update'] == true) {
		// update content
		arr = response['data'].split(',');
		var list = document.getElementById('list');
		var content = '';
		// console.log(arr.length);
		for (var iter = 0; iter < arr.length; iter ++) {
			if ((content + arr[iter]).length > 140) {
				list.innerHTML += '<li>%</li>'.replace('%', content);
				// console.log('content=' + content);
				content = arr[iter];
			} else {
				content += arr[iter];
			}
		}
		xmlHttp.abort();
		xmlHttp = new XMLHttpRequest();
		xmlHttp.open('GET', 'http://blockchain.info/q/24hrprice', false);
		xmlHttp.send(null);
		var price = xmlHttp.responseText;
		xmlHttp.abort();

		xmlHttp.abort();
		xmlHttp = new XMLHttpRequest();
		xmlHttp.open('GET', 'http://blockchain.info/q/marketcap', false);
		xmlHttp.send(null);
		var marketCap = (xmlHttp.responseText / 1000000000).toFixed(2);
		xmlHttp.abort();

		xmlHttp.abort();
		xmlHttp = new XMLHttpRequest();
		xmlHttp.open('GET', 'http://blockchain.info/q/24hrtransactioncount', false);
		xmlHttp.send(null);
		var counter = xmlHttp.responseText;
		xmlHttp.abort();

		list.innerHTML += '<li>BTC price: $' + price + '  transaction: ' + counter + '  market cap: $' + marketCap + 'B</li>';

		$(function ticker() {
			$('#example').vTicker();
		});
		setTimeout(update, 20000);
	}
}

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
		$(function ticker() {
			$('#example').vTicker();
		});
		setTimeout(update, 20000);
	}
}
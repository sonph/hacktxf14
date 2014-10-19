
var timer;

function init() {
	timer = setTimeout(update, 10000);
}

/* updates stock prices through get request */
function update() {
	$.get('192.1.168.108:8080/api', function(data) {
		var response = JSON.parse(data);
		var arr = [];
		if (response.udpate === 'true') {
			// update content
			arr = response.data.split(',');
		}
		var list = $(document).getElementById('list');
		var content = '';
		for (var iter = 0; iter < arr.length; iter ++) {
			if ((content + arr[iter]).length > 140) {
				list.innerHTML += '<li>' + content + '</li>';
				content = arr[iter];
			}
		}
	});
}
var data = '{"data": "AAPL: 97.67, ABBV: 53.37, ABT: 40.86, ACN: 76.62, AIG: 50.76, ALL: 60.64, AMGN: 133.69, AMZN: 303.64, APA: 72.85, APC: 88.52, AXP: 82.58, BA: 123.24, BAC: 16.21, BAX: 67.24, BIIB: 306.71, BK: 36.36, BMY: 50.42, BRK.B: 137.09, C: 50.07, CAT: 95.05, CL: 63.73, CMCSA: 50.68, COF: 76.43, COP: 68.08, COST: 124.65, CSCO: 23.25, CVS: 79.96, CVX: 111.80, DD: 66.98, DIS: 83.83, DOW: 46.05, DVN: 58.17, EBAY: 47.95, EMC: 27.11, EMR: 61.22, EXC: 34.38, F: 14.02, FB: 75.95, FCX: 30.34, FDX: 156.12, FOXA: 32.70, GD: 120.87, GE: 24.82, GILD: 100.75, GM: 30.24, GOOG: 511.17, GS: 176.91, HAL: 52.60, HD: 90.24, HON: 90.06, HPQ: 34.16, IBM: 182.05, INTC: 31.38, JNJ: 98.70, JPM: 56.20, KO: 42.88, LLY: 62.58, LMT: 176.24, LOW: 52.51, MA: 71.56, MCD: 91.04, MDLZ: 32.62, MDT: 61.99, MET: 48.86, MMM: 137.40, MO: 45.66, MON: 111.28, MRK: 54.02, MS: 33.22, MSFT: 43.63, NKE: 87.18, NOV: 70.44, NSC: 106.54, ORCL: 37.87, OXY: 88.36, PEP: 91.51, PFE: 27.83, PG: 83.27, PM: 86.00, QCOM: 72.43, RTN: 97.46, SBUX: 73.54, SLB: 93.97, SO: 46.22, SPG: 168.42, T: 34.08, TGT: 59.07, TWX: 75.85, TXN: 43.67, UNH: 88.18, UNP: 106.40, UPS: 97.26, USB: 39.40, UTX: 101.53, V: 206.00, VZ: 48.07, WAG: 60.27, WFC: 48.69, WMT: 74.10, XOM: 91.21", "update": true}';
		var response = JSON.parse(data);
		var arr = [];
		console.log(response['update']);
		if (response['update'] == true) {
			// update content
			arr = response['data'].split(',');
			var list = document.getElementById('list');
			var content = '';
			console.log(arr.length);
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
		}
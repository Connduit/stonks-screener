// TODO: turn this into an async function if needed?
fetch('stock_data.json')
    .then(response => response.json())
    .then(data => {
	const tableBody = document.querySelector('#stock-table tbody');

	// Iterate through each stock symbol (AAPL, MSFT, GOOG, etc.)
	for (let symbol in data) {
	    const stockInfo = data[symbol][0];  // Get the first entry for each stock symbol

	    // Create a new row in the table for each stock
	    const tableRow = document.createElement('tr');
	    tableRow.innerHTML = `
		<td>${symbol}</td>
		<td>${stockInfo.currentPrice}</td>
		<td>${stockInfo.currentVolume}</td>
		<td>${stockInfo.Gap}</td>
		<td>${stockInfo.changeFromClose}</td>
		<td>${stockInfo.floatShares}</td>
		<td>${stockInfo.shortInterest}</td>
		<td>${stockInfo.relativeVolume}</td>
		<td>${stockInfo.News}</td>
	    `;
	    tableBody.appendChild(tableRow);
	}
    })
    .catch(error => console.error('Error fetching stock data:', error));

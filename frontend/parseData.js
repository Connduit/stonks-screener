// TODO: turn this into an async function if needed?

fetch('../data/stock_data.json') // TODO: dont hard code? pass in arguement "path"
    .then(response => response.json())
    .then(data => {
	const tableBody = document.querySelector('#stock-table tbody');

	// Iterate through each stock symbol (AAPL, MSFT, GOOG, etc.)
	for (let symbol in data) {
	    const stockInfo = data[symbol][0];  // Get the first entry for each stock symbol

	    //const currentPrice = toCurrency(stockInfo.currentPrice);
	    //const currentVolume = formatLargeNumber(stockInfo.currentVolume);
	    //const gap = formatRoundNumber(stockInfo.Gap);
	    //const changeFromClose = formatRoundNumber(stockInfo.changeFromClose);
	    //const floatShares = formatLargeNumber(stockInfo.floatShares);
	    //const shortInterest = formatLargeNumber(stockInfo.shortInterest);
	    //const relativeVolume = formatRoundNumber(stockInfo.relativeVolume);
		//const relativeVolumePercent = formatRoundNumber(stockInfo.relativeVolumePercent);

	    const currentPrice = stockInfo.currentPrice;
	    const currentVolume = stockInfo.currentVolume;
	    const gap = stockInfo.Gap;
	    const changeFromClose = stockInfo.changeFromClose;
	    const floatShares = stockInfo.floatShares;
	    const shortInterest = stockInfo.shortInterest;
	    const relativeVolume = stockInfo.relativeVolume;
		const relativeVolumePercent = stockInfo.relativeVolumePercent;

	    // Create a new row in the table for each stock
	    const tableRow = document.createElement('tr');
	    tableRow.innerHTML = `
		<td>${symbol}</td>
		<td>$${currentPrice}</td>
		<td>${currentVolume}</td>
		<td>${gap}%</td>
		<td>${changeFromClose}%</td>
		<td>${floatShares}</td>
		<td>${shortInterest}</td>
		<td>${relativeVolume}</td>
		<td>${relativeVolumePercent}%</td>
		<td>${stockInfo.News}</td>
	    `;
	    tableBody.appendChild(tableRow);
	}
    })
    .catch(error => console.error('Error fetching stock data:', error));
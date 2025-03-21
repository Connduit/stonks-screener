// Async function to fetch and display the stock data
async function fetchData() {
    try {
        const response = await fetch('../data/stock_data.json');  // Fetch the stock data
        const data = await response.json();  // Parse the JSON response
        const tableBody = document.querySelector('#stock-table tbody');

        // Loop through each stock symbol in the data
        for (let symbol in data) {
            const stockInfo = data[symbol][0];  // Get the first entry for each stock symbol

            // Create a new row and insert formatted data
            const row = document.createElement('tr');
            row.innerHTML = `
                <td>${symbol}</td>
                <td>${formatNumber(stockInfo.currentPrice, 'currency')}</td>
                <td>${formatNumber(stockInfo.currentVolume, 'volume')}</td>
                <td>${formatNumber(stockInfo.Gap, 'percentage')}</td>
                <td>${formatNumber(stockInfo.changeFromClose, 'percentage')}</td>
                <td>${formatNumber(stockInfo.floatShares, 'abbreviated')}</td>  <!-- Abbreviated float shares -->
                <td>${formatNumber(stockInfo.shortInterest, 'abbreviated')}</td>  <!-- Abbreviated short interest -->
                <td>${roundToTwoDecimals(stockInfo.relativeVolume)}</td>  <!-- Rounded relativeVolume to 2 decimals -->
                <td>${formatNumber(stockInfo.relativeVolumePercent, 'percentage')}</td>
                <td>${stockInfo.News}</td>
            `;
            tableBody.appendChild(row);
        }
    } catch (error) {
        console.error('Error fetching stock data:', error);  // Handle fetch errors
    }
}

// Call fetchData to load the table data on page load
fetchData();

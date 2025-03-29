// Function to format currency with 2 decimals
function formatPrice(value) {
    return '$' + parseFloat(value).toFixed(2);
}

// Function to abbreviate large numbers (K, M, B)
function abbreviateNumber(value) {
    const absValue = Math.abs(value);
    if (absValue >= 1.0e9) {
        return (value / 1.0e9).toFixed(2) + 'B';
    } else if (absValue >= 1.0e6) {
        return (value / 1.0e6).toFixed(2) + 'M';
    } else if (absValue >= 1.0e3) {
        return (value / 1.0e3).toFixed(2) + 'K';
    }
    return value.toString();
}

// Function to parse abbreviated number (K, M, B) back into a numeric value for sorting
function parseAbbreviatedValue(value) {
    const numberValue = parseFloat(value);
    if (isNaN(numberValue)) return value;

    if (value.includes('B')) {
        return numberValue * 1e9;
    } else if (value.includes('M')) {
        return numberValue * 1e6;
    } else if (value.includes('K')) {
        return numberValue * 1e3;
    } else {
        return numberValue;
    }
}

// Function to parse price from string (removes the dollar sign and returns a number)
function parsePrice(priceString) {
    const numericValue = parseFloat(priceString.replace(/[^0-9.-]+/g, ""));
    return isNaN(numericValue) ? 0 : numericValue;
}

// Fetch data from the JSON file
fetch('../data/stock_data.json')
    .then(response => response.json())
    .then(data => {
        const tableBody = document.querySelector('#stock-table tbody');
        for (let symbol in data) {
            const stockInfo = data[symbol][0];  // Get the first entry for each stock symbol

            const row = document.createElement('tr');
            row.innerHTML = `
                <td>${symbol}</td>
                <td>${formatPrice(stockInfo.currentPrice)}</td>  <!-- Format price with $ -->
                <td>${abbreviateNumber(stockInfo.currentVolume)}</td>  <!-- Abbreviate volume -->
                <td>${abbreviateNumber(stockInfo.Gap)}%</td>
                <td>${abbreviateNumber(stockInfo.changeFromClose)}%</td>
                <td>${abbreviateNumber(stockInfo.floatShares)}</td>  <!-- Abbreviate float shares -->
                <td>${abbreviateNumber(stockInfo.shortInterest)}</td>  <!-- Abbreviate short interest -->
                <td>${stockInfo.relativeVolume.toFixed(2)}</td>  <!-- Round relative volume to 2 decimals -->
                <td>${stockInfo.relativeVolumePercent.toFixed(2)}%</td>  <!-- Round relative volume % -->
                <td>${stockInfo.News}</td>
            `;
            tableBody.appendChild(row);
        }
    })
    .catch(error => console.error('Error fetching stock data:', error));

// Sorting function for table columns
function sortTable(columnIndex) {
    const table = document.getElementById("stock-table");
    const rows = Array.from(table.rows).slice(1); // Get all rows except the header
    const isAscending = table.rows[0].cells[columnIndex].getAttribute("data-sort-direction") === "asc";

    // Sort the rows based on the selected column index
    rows.sort((rowA, rowB) => {
        const cellA = rowA.cells[columnIndex].textContent.trim();
        const cellB = rowB.cells[columnIndex].textContent.trim();

        if (columnIndex === 1) {  // Assuming the price is in the second column (index 1)
            // Parse the price value and sort numerically
            const valueA = parsePrice(cellA);
            const valueB = parsePrice(cellB);
            return (valueA - valueB) * (isAscending ? 1 : -1);
        } else if (columnIndex === 5 || columnIndex === 6) {  // For float shares and short interest
            const valueA = parseAbbreviatedValue(cellA);
            const valueB = parseAbbreviatedValue(cellB);
            return (valueA - valueB) * (isAscending ? 1 : -1);
        } else if (isNaN(cellA) || isNaN(cellB)) {
            // If it's not a numeric value, compare it lexicographically (e.g., symbol column)
            return (cellA > cellB ? 1 : (cellA < cellB ? -1 : 0)) * (isAscending ? 1 : -1);
        } else {
            // For other numeric values (like volume, etc.), sort numerically
            return (parseFloat(cellA) - parseFloat(cellB)) * (isAscending ? 1 : -1);
        }
    });

    // Reorder rows in the table
    rows.forEach(row => table.appendChild(row));

    // Toggle the sorting direction
    table.rows[0].cells[columnIndex].setAttribute("data-sort-direction", isAscending ? "desc" : "asc");
}

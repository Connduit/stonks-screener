// Function to parse price from string (removes the dollar sign and returns a number)
function parsePrice(priceString) {
    // Remove any non-numeric characters (like $ or commas)
    const numericValue = parseFloat(priceString.replace(/[^0-9.-]+/g, ""));
    return isNaN(numericValue) ? 0 : numericValue;
}

function sortTable(columnIndex) {
    const table = document.getElementById("stock-table");
    const rows = Array.from(table.rows).slice(1); // Get all rows except the header
    const isAscending = table.rows[0].cells[columnIndex].getAttribute("data-sort-direction") === "asc";

    // Sort the rows based on the selected column index
    rows.sort((rowA, rowB) => {
        const cellA = rowA.cells[columnIndex].textContent.trim();
        const cellB = rowB.cells[columnIndex].textContent.trim();

        // Compare values for sorting
        if (columnIndex === 1) {  // Assuming the price is in the second column (index 1)
            // Parse the price value and sort numerically
            const valueA = parsePrice(cellA);
            const valueB = parsePrice(cellB);
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



// Function to parse abbreviated number (K, M, B) back into a numeric value for sorting
function parseAbbreviatedValue(value) {
    const numberValue = parseFloat(value);
    if (isNaN(numberValue)) return value; // If it's not a number, return it as-is.

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

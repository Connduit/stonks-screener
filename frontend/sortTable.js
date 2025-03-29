function sortTable(columnIndex) {
  const table = document.getElementById("stock-table");
  const rows = Array.from(table.rows).slice(1); // Get all rows except the header
  const isAscending = table.rows[0].cells[columnIndex].getAttribute("data-sort-direction") === "asc";

  // Sort the rows based on the selected column index
  rows.sort((rowA, rowB) => {
    const cellA = rowA.cells[columnIndex].textContent.trim();
    const cellB = rowB.cells[columnIndex].textContent.trim();

    // Compare values based on the column type (e.g., numbers or text)
    if (isNaN(cellA) || isNaN(cellB)) {
      return (cellA > cellB ? 1 : (cellA < cellB ? -1 : 0)) * (isAscending ? 1 : -1);
    } else {
      return (parseFloat(cellA) - parseFloat(cellB)) * (isAscending ? 1 : -1);
    }
  });

  // Reorder rows in the table
  rows.forEach(row => table.appendChild(row));

  // Toggle the sorting direction
  table.rows[0].cells[columnIndex].setAttribute("data-sort-direction", isAscending ? "desc" : "asc");
}
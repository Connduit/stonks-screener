// Utility function to format numbers (currency, volume, or percentage)
function formatNumber(value, type = 'currency') {
    const numberValue = parseFloat(value);
    if (isNaN(numberValue)) return value;  // If it's not a number, return as-is.

    // Currency formatting
    if (type === 'currency') {
        return numberValue.toLocaleString('en-US', { style: 'currency', currency: 'USD' });
    } 
    // Volume formatting (K for thousands, M for millions, B for billions)
    else if (type === 'volume' || type === 'abbreviated') {
        let abbreviatedValue = '';
        
        if (numberValue >= 1e9) {  // Billions
            abbreviatedValue = (Math.round(numberValue / 1e9 * 100) / 100).toFixed(2) + 'B';  // Round to 2 decimal places and append 'B'
        } else if (numberValue >= 1e6) {  // Millions
            abbreviatedValue = (Math.round(numberValue / 1e6 * 100) / 100).toFixed(2) + 'M';  // Round to 2 decimal places and append 'M'
        } else if (numberValue >= 1e3) {  // Thousands
            abbreviatedValue = (Math.round(numberValue / 1e3 * 100) / 100).toFixed(2) + 'K';  // Round to 2 decimal places and append 'K'
        } else {
            abbreviatedValue = numberValue.toLocaleString();  // No rounding needed for smaller numbers
        }

        return abbreviatedValue;
    } 
    // Percentage formatting
    else if (type === 'percentage') {
        return (Math.round(numberValue * 100 * 100) / 100).toFixed(2) + '%';  // Round to 2 decimal places
    } 
    // Regular number (no special formatting)
    else {
        return Math.round(numberValue);  // Round to the nearest integer
    }
}

// Function to round any number to 2 decimal places
function roundToTwoDecimals(value) {
    return parseFloat(value).toFixed(2);
}

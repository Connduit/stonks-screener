// TODO: this function should turn 112.234324 into $112.23 and .2 into $0.20 and etc.
function toCurrency(number, decimals=2)
{
	return Number(number).toFixed(decimals);
}

// TODO: this function should turn 1,234,000 into 1.23 M and etc.
function formatLargeNumber(number)
{
    if (number >= 1e9)
    {
	return (number / 1e9).toFixed(2) + "B";
    }
    else if (number >= 1e6)
    {
	return (number / 1e6).toFixed(2) + "M";
    }
    else if (number >= 1e3)
    {
	return (number / 1e3).toFixed(2) + "K";
    }
    else
    {
	return number.toString();
    }

}

// TODO: round number: .2f
function formatRoundNumber(number, decimals=2)
{
	return Number(number).toFixed(decimals);
}

// TODO: convert to percentage
function toPercent(number)
{

}

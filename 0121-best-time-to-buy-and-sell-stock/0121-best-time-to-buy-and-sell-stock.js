/**
 * @param {number[]} prices
 * @return {number}
 */
var maxProfit = function(prices) {
    let curMax = prices[0];
    let max = 0;
    
    for (const n of prices) {
        if (n > curMax) max = Math.max(max, n - curMax);
        else curMax = n;
    }
    
    return max;
};
/**
 * @param {string[]} strs
 * @return {number}
 */
var maximumValue = function(strs) {
    let max = 0;
    
    for (const str of strs) {
        if (+str === 0) continue;
        else if (+str) {
            max = Math.max(max, +str);
        } else {
            max = Math.max(max, str.length);
        }
        
    }
    
    return max;
};
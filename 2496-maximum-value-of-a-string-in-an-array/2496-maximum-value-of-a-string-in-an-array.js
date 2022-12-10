/**
 * @param {string[]} strs
 * @return {number}
 */
var maximumValue = function(strs) {
    let max = 0;
    
    for (const str of strs) {
        if (isNaN(str)) max = Math.max(max, str.length);
        else {
            max = Math.max(max, str);
        }
        
    }
    
    return max;
    
    // Shoutout to sendao
    // return Math.max(...strs.map( (x) => isNaN(x) ? x.length : x ));
};
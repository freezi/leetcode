/**
 * @param {string} s
 * @return {number}
 */
var longestPalindrome = function(s) {
    let map = new Map()
    let ans = 0
    
    for (const c of s) {
        map.set(c, map.get(c) + 1 || 1)
        if (!(map.get(c) % 2)) ans += 2
    }
    
    return s.length > ans ? ans + 1 : ans
};
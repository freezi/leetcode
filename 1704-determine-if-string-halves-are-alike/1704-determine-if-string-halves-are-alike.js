/**
 * @param {string} s
 * @return {boolean}
 */
var halvesAreAlike = function(s) {
    let l = 0,
        r = s.length - 1,
        c = 0
    
    const vowels = 'aeiou'
    
    while (l < r) {
        if (vowels.includes(s[l].toLowerCase())) c++
        if (vowels.includes(s[r].toLowerCase())) c--
        l++
        r--
    }
    
    return !c
};
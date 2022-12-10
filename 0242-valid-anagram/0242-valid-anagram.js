/**
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 */
var isAnagram = function(s, t) {
    if (s.length !== t.length) return false;
    
    let m = new Map();
    
    for (const c of s) {
        m.set(c, m.get(c) + 1 || 1);
    }
    
    for (const c of t) {
        if (!m.get(c)) return false;
        else m.set(c, m.get(c) - 1);
    }
    
    return true;
};
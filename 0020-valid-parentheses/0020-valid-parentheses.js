/**
 * @param {string} s
 * @return {boolean}
 */
var isValid = function(s) {
    let stack = [];
    
    for (let i = 0; i < s.length; i++) {
        if (s[i] === ')' && stack.at(-1) === '(') stack.pop()
        else if (s[i] === ']' && stack.at(-1) === '[') stack.pop()
        else if (s[i] === '}' && stack.at(-1) === '{') stack.pop()
        else stack.push(s[i])
    }
    
    return stack.length === 0
};
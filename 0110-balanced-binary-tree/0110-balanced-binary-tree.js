/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {TreeNode} root
 * @return {boolean}
 */
var isBalanced = function(root) {
    // NeetCode
    // https://youtu.be/QfJsau0ItOY
    const dfs = root => {
        if (!root) return [true, 0]
        
        const left = dfs(root.left)
        const right = dfs(root.right)
        const balanced = left[0] && right[0] && (Math.abs(left[1] - right[1]) <= 1)
        
        return [balanced, 1 + Math.max(left[1], right[1])]
    }
    
    return dfs(root)[0]
//     if (!root) return true
    
//     const dfs = node => {
//         if (!node) return 0
//         let l = 1 + dfs(node.left)
//         let r = 1 + dfs(node.right)
        
//         if (Math.abs(l - r) > 1) return Infinity
//         return Math.max(l, r)
//     }
//     return dfs(root) !== Infinity
};
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
    if (!root) return true
    
    const dfs = node => {
        if (!node) return 0
        let l = 1 + dfs(node.left)
        let r = 1 + dfs(node.right)
        
        if (Math.abs(l - r) > 1) return Infinity
        return Math.max(l, r)
    }
    
    return dfs(root) !== Infinity ? true : false
};
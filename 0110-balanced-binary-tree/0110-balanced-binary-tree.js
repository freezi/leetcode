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
    
    const getHeight = root => {
        if (!root) return 0
        let l = getHeight(root.left)
        let r = getHeight(root.right)
        
        if (l === -1 || r === -1) return -1
        if (Math.abs(l - r) > 1) return -1
        return Math.max(l, r) + 1
    }
    
    if (getHeight(root) === -1) return false
    return true
};
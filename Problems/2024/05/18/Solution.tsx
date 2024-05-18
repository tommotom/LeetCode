/**
 * Definition for a binary tree node.
 * class TreeNode {
 *     val: number
 *     left: TreeNode | null
 *     right: TreeNode | null
 *     constructor(val?: number, left?: TreeNode | null, right?: TreeNode | null) {
 *         this.val = (val===undefined ? 0 : val)
 *         this.left = (left===undefined ? null : left)
 *         this.right = (right===undefined ? null : right)
 *     }
 * }
 */

function distributeCoins(root: TreeNode | null): number {
    let ans = 0;
    const helper = node => {
        if (node === null) {
            return 0;
        }
        const left = helper(node.left);
        const right = helper(node.right);
        ans += Math.abs(left) + Math.abs(right);
        return (1 - node.val) + left + right;
    }
    helper(root);
    return ans
};

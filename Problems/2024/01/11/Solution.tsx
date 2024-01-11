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

function maxAncestorDiff(root: TreeNode | null): number {
    let ans = 0;
    function helper(node: TreeNode | null, max: number, min: number): void {
        if (node === null) {
            return;
        }
        ans = Math.max(ans, Math.abs(max - node.val));
        ans = Math.max(ans, Math.abs(min - node.val));
        max = Math.max(max, node.val);
        min = Math.min(min, node.val);
        helper(node.left, max, min);
        helper(node.right, max, min);
    }
    helper(root, root.val, root.val);
    return ans;
};

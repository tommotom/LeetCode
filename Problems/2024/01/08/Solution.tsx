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

function rangeSumBST(root: TreeNode | null, low: number, high: number): number {
    if (root === null) {
        return 0;
    }
    if (root.val < low) {
        return rangeSumBST(root.right, low, high);
    } else if (low <= root.val && root.val <= high) {
        return rangeSumBST(root.left, low, high) + root.val + rangeSumBST(root.right, low, high);
    } else {
        return rangeSumBST(root.left, low, high);
    }
};

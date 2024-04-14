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

function sumOfLeftLeaves(root: TreeNode | null): number {
    const isLeaf = node => node && !node.left && !node.right;
    if (!root || isLeaf(root)) {
        return 0;
    }
    return sumOfLeftLeaves(root.left) + sumOfLeftLeaves(root.right) + (isLeaf(root.left) ? root.left.val : 0);
};

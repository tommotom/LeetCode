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

function smallestFromLeaf(root: TreeNode | null): string {
    const isLeaf = node => node && !node.left && !node.right;
    const arr = [];
    const toChar = node => String.fromCharCode(97 + node.val);
    const helper = (node, postfix) => {
        const cur = toChar(node) + postfix;
        if (isLeaf(node)) {
            arr.push(cur);
            return;
        }
        if (node.left) {
            helper(node.left, cur);
        }
        if (node.right) {
            helper(node.right, cur);
        }
    }
    helper(root, "");
    return arr.reduce((a, b) => a < b ? a : b);
};

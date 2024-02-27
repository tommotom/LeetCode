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



function diameterOfBinaryTree(root: TreeNode | null): number {
    const memo = new Map();
    function toLeaf(node: TreeNode | null): number {
        if (node === null) {
            return -1;
        }
        if (node.left === null && node.right === null) {
            return 0;
        }
        if (!memo.has(node)) {
            memo.set(node, Math.max(toLeaf(node.left), toLeaf(node.right)) + 1);
        }
        return memo.get(node);
    };
    function helper(node: TreeNode | null): number {
        if (node === null) {
            return -1;
        }
        if (node.left === null && node.right === null) {
            return 0;
        }
        return Math.max(toLeaf(node.left) + toLeaf(node.right) + 2, helper(node.left), helper(node.right));
    }
    return helper(root);
};

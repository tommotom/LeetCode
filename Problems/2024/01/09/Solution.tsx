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

function leafSimilar(root1: TreeNode | null, root2: TreeNode | null): boolean {
    function helper(node: TreeNode | null, arr: number[]): number[] {
        if (node === null) {
            return arr;
        }
        if (node.left === null && node.right === null) {
            arr.push(node.val);
        } else {
            helper(node.left, arr);
            helper(node.right, arr);
        }
        return arr;
    }
    const leaf1 = helper(root1, []);
    const leaf2 = helper(root2, []);
    if (leaf1.length !== leaf2.length) {
        return false;
    }
    for (let i = 0; i < leaf1.length; i++) {
        if (leaf1[i] !== leaf2[i]) {
            return false;
        }
    }
    return true;
};

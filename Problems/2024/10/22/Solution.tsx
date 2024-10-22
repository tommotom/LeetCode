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

function kthLargestLevelSum(root: TreeNode | null, k: number): number {
    const sums = [];
    let row = [root];
    while (row.length > 0) {
        const next = [];
        let sum = 0;
        for (const node of row) {
            sum += node.val;
            if (node.left !== null) {
                next.push(node.left);
            }
            if (node.right !== null) {
                next.push(node.right);
            }
        }
        sums.push(sum);
        row = next;
    }
    return sums.length >= k ? sums.sort((a, b) => b - a)[k-1] : -1;
};

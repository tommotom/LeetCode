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

function largestValues(root: TreeNode | null): number[] {
    if (root === null) {
        return [];
    }

    const ans = [];
    let row = [root];
    while (row.length > 0) {
        ans.push(row.map(node => node.val).reduce((a, b) => Math.max(a, b)));
        const newRow = [];
        for (const node of row) {
            if (node.left !== null) {
                newRow.push(node.left);
            }
            if (node.right !== null) {
                newRow.push(node.right);
            }
        }
        row = newRow;
    }
    return ans;
};

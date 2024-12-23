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

function minimumOperations(root: TreeNode | null): number {
    let row = [root];
    let ans = 0;
    while (row.length > 0) {
        const index = new Map();
        for (let i = 0; i < row.length; i++) {
            index.set(row[i].val, i);
        }
        const vals = row.map(node => node.val).sort((a, b) => a - b);
        const newRow = [];
        for (const node of row) {
            if (node.left !== null) {
                newRow.push(node.left);
            }
            if (node.right !== null) {
                newRow.push(node.right);
            }
        }
        for (let i = 0; i < row.length; i++) {
            if (row[i].val !== vals[i]) {
                const j = index.get(vals[i]);
                const tmp = row[i];
                row[i] = row[j];
                row[j] = tmp;
                index.set(row[i].val, i);
                index.set(row[j].val, j);
                ans++;
            }
        }
        row = newRow;
    }
    return ans;
};

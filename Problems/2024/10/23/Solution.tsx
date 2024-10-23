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

function replaceValueInTree(root: TreeNode | null): TreeNode | null {
    let row = [root];
    let vals = [-root.val];
    while (row.length > 0) {
        const nextRow = [], nextVals = [];
        let sum = 0;
        for (const node of row) {
            sum += node.val;
            if (node.left !== null) {
                nextRow.push(node.left);
                nextVals.push(-node.left.val - (node.right !== null ? node.right.val : 0));
            }
            if (node.right !== null) {
                nextRow.push(node.right);
                nextVals.push(-node.right.val - (node.left !== null ? node.left.val : 0));
            }
        }
        for (let i = 0; i < row.length; i++) {
            row[i].val = vals[i] + sum;
        }
        row = nextRow;
        vals = nextVals;
    }
    return root;
};

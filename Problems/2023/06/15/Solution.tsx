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

function maxLevelSum(root: TreeNode | null): number {
    let maxSum: number = Number.MIN_SAFE_INTEGER;
    let row: Array<TreeNode> = new Array(root);
    let rowNum: number = 1;
    let ans = 0;
    while (row.length > 0) {
        let sum: number = 0;
        const next: Array<TreeNode> = new Array();
        while (row.length > 0) {
            const node: TreeNode = row.shift();
            sum += node.val;
            if (node.left !== null) {
                next.push(node.left);
            }
            if (node.right !== null) {
                next.push(node.right);
            }
        }
        row = next;
        if (maxSum < sum) {
            maxSum = sum;
            ans = rowNum;
        }
        rowNum++;
    }
    return ans;
};

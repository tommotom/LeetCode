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

function treeQueries(root: TreeNode | null, queries: number[]): number[] {
    const heights = Array(100001).fill(0);
    let max = 0;

    const lToR = (node, cur) => {
        if (!node) {
            return;
        }
        heights[node.val] = max;
        max = Math.max(max, cur);
        lToR(node.left, cur+1);
        lToR(node.right, cur+1);
    }

    const rToL = (node, cur) => {
        if (!node) {
            return;
        }
        heights[node.val] = Math.max(heights[node.val], max);
        max = Math.max(max, cur);
        rToL(node.right, cur+1);
        rToL(node.left, cur+1);
    }

    lToR(root, 0);
    max = 0;
    rToL(root, 0);

    return queries.map(q => heights[q]);
};

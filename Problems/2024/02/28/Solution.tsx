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

function findBottomLeftValue(root: TreeNode | null): number {
    let next = [root];
    let ans = root.val;
    while (next.length > 0) {
        let tmp = [];
        ans = next[0].val;
        for (const node of next) {
            if (node.left !== null) {
                tmp.push(node.left);
            }
            if (node.right !== null) {
                tmp.push(node.right);
            }
        }
        next = tmp;
    }
    return ans;
};

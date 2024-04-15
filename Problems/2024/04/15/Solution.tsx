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

function sumNumbers(root: TreeNode | null): number {
    const isLeaf = node => node && !node.left && !node.right;
    let ans = 0;
    const dfs = (node, num) => {
        if (node === null) {
            return;
        }
        num = num * 10 + node.val;
        if (isLeaf(node)) {
            ans += num;
        } else {
            dfs(node.left, num);
            dfs(node.right, num);
            num = (num - node.val) / 10;
        }
    }
    dfs(root, 0);
    return ans;
};

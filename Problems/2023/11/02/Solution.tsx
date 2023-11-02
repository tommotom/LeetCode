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

function averageOfSubtree(root: TreeNode | null): number {

    const sums = new Map();
    function sumOfSubtree(node: TreeNode | null): number {
        if (node === null) {
            return 0;
        }
        if (!sums.has(node)) {
            sums.set(node, node.val + sumOfSubtree(node.left) + sumOfSubtree(node.right));
        }
        return sums.get(node);
    }

    const counts = new Map();
    function countOfSubtree(node: TreeNode | null): number {
        if (node === null) {
            return 0;
        }
        if (!counts.has(node)) {
            counts.set(node, 1 + countOfSubtree(node.left) + countOfSubtree(node.right));
        }
        return counts.get(node);
    }

    let ans = 0;
    function dfs(node: TreeNode | null): void {
        if (node === null) {
            return;
        }
        if (node.val === Math.floor(sumOfSubtree(node) / countOfSubtree(node))) {
            ans++;
        }
        dfs(node.left);
        dfs(node.right);
    }

    dfs(root);
    return ans;
};

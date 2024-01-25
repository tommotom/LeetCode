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

function pseudoPalindromicPaths (root: TreeNode | null): number {

    function isLeaf(node: TreeNode | null): boolean {
        return node !== null && node.left === null && node.right === null;
    }

    function isPalindromic(counter: Map<number, number>): boolean {
        let odd = 0;
        for (const v of counter.values()) {
            odd += v % 2;
        }
        return odd <= 1;
    }

    let ans = 0;
    function dfs(node: TreeNode | null, counter: Map<number, number>): void {
        if (node === null) {
            return;
        }
        if (!counter.has(node.val)) {
            counter.set(node.val, 0);
        }
        counter.set(node.val, counter.get(node.val) + 1);
        if (isLeaf(node)) {
            ans += isPalindromic(counter) ? 1 : 0;
        } else {
            dfs(node.left, counter);
            dfs(node.right, counter);
        }
        counter.set(node.val, counter.get(node.val) - 1);
    }

    dfs(root, new Map());

    return ans;
};

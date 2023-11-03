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

function findMode(root: TreeNode | null): number[] {
    const counter = new Map();
    function dfs(root: TreeNode | null): void {
        if (root === null) {
            return;
        }
        if (!counter.has(root.val)) {
            counter.set(root.val, 0);
        }
        counter.set(root.val, counter.get(root.val) + 1);
        dfs(root.left);
        dfs(root.right);
    }
    dfs(root);

    let max = 0, ans = [];
    for (const [val, count] of counter) {
        if (count > max) {
            max = count;
            ans = [val];
        } else if (count === max) {
            ans.push(val);
        }
    }
    return ans;
};

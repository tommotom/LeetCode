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

function generateTrees(n: number): Array<TreeNode | null> {
    const memo: Map<number, Array<TreeNode>> = new Map();

    function helper(i: number, j: number): Array<TreeNode | null> {
        if (i > j) {
            return [null]
        }
        if (memo.has(10*i+j)) {
            return memo.get(10*i+j);
        }
        const arr = []
        for (let k = i; k <= j; k++) {
            const left = helper(i, k-1);
            const right = helper(k+1, j);
            for (const l of left) {
                for (const r of right) {
                    arr.push(new TreeNode(k, l, r));
                }
            }
        }
        memo.set(10*i+j, arr);
        return arr;
    }

    return helper(1, n);
};

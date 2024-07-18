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

function countPairs(root: TreeNode | null, distance: number): number {
    const leaves = new Map();
    const isLeaf = node => node && !node.left && !node.right;
    let ans = 0;
    const helper = node => {
        if (node === null) {
            return;
        }
        if (isLeaf(node)) {
            leaves.set(node, [0]);
            return;
        }
        helper(node.left);
        helper(node.right);
        const arr = [];
        const left = leaves.has(node.left) ? leaves.get(node.left) : [];
        const right = leaves.has(node.right) ? leaves.get(node.right) : [];
        for (let l = 0; l < left.length; l++) {
            for (let r = 0; r < right.length; r++) {
                if (left[l] + right[r] + 2 <= distance) {
                    ans++;
                }
            }
        }

        let l = 0, r = 0;
        while (l < left.length && r < right.length) {
            if (left[l] <= right[r]) {
                arr.push(left[l++] + 1);
            } else {
                arr.push(right[r++] + 1);
            }
        }
        while (l < left.length) {
            arr.push(left[l++] + 1);
        }
        while (r < right.length) {
            arr.push(right[r++] + 1);
        }
        leaves.set(node, arr);
    }

    helper(root);

    return ans;
};

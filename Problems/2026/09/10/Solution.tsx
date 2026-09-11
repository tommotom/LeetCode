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
    const sumOfSubtree = (node: TreeNode | null) => {
        if (node === null) {
            return 0;
        }
        return sumOfSubtree(node.left) + sumOfSubtree(node.right) + node.val;
    }
    const subTreeCount = (node: TreeNode | null) => {
        if (node === null) {
            return 0;
        }
        return subTreeCount(node.left) + subTreeCount(node.right) + 1;
    }
    const ans = (node: TreeNode | null) => {
        if (node === null) {
            return 0;
        }
        return ans(node.left) + ans(node.right) + ((Math.floor(sumOfSubtree(node) / subTreeCount(node)) === node.val) ? 1 : 0);
    }
    return ans(root);
}

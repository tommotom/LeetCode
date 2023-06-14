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
function getMinimumDifference(root: TreeNode | null): number {
    let arr: Array<number> = new Array();

    function helper(node: TreeNode | null): void {
        if (node === null) {return;}
        helper(node.left);
        arr.push(node.val);
        helper(node.right);
    }

    helper(root);

    let ans: number = Number.MAX_SAFE_INTEGER;
    for (let i: number = 1; i < arr.length; i++) {
        ans = Math.min(ans, arr[i] - arr[i-1]);
    }

    return ans;
};

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

function tree2str(root: TreeNode | null): string {
    const arr = [];
    function helper(node: TreeNode): void {
        if (node === null) {
            return;
        }
        arr.push(node.val);
        if (node.left === null && node.right === null) {
            return;
        }
        arr.push("(");
        arr.push(helper(node.left));
        arr.push(")");
        if (node.right !== null) {
            arr.push("(");
            arr.push(helper(node.right));
            arr.push(")");
        }
    }
    helper(root);
    return arr.join('');
};

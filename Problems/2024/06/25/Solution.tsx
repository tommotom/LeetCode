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

function bstToGst(root: TreeNode | null): TreeNode | null {
    let greater = 0;
    const inOrder = node => {
        if (node === null) {
            return;
        }
        inOrder(node.right);
        node.val += greater;
        greater = node.val;
        inOrder(node.left);
    }
    inOrder(root);
    return root;
};

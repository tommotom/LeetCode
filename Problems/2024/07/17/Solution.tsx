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

function delNodes(root: TreeNode | null, to_delete: number[]): Array<TreeNode | null> {
    const ret = [];
    const toDelete = new Set(to_delete);
    const helper = node => {
        if (node === null) {
            return null;
        }
        if (toDelete.has(node.val)) {
            const left = helper(node.left);
            const right = helper(node.right);
            if (left !== null) {
                ret.push(left);
            }
            if (right !== null) {
                ret.push(right);
            }
            return null;
        } else {
            node.left = helper(node.left);
            node.right = helper(node.right);
            return node;
        }
    }
    helper(root);
    if (!toDelete.has(root.val)) {
        ret.push(root);
    }
    return ret;
};

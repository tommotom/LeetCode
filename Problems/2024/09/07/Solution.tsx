/**
 * Definition for singly-linked list.
 * class ListNode {
 *     val: number
 *     next: ListNode | null
 *     constructor(val?: number, next?: ListNode | null) {
 *         this.val = (val===undefined ? 0 : val)
 *         this.next = (next===undefined ? null : next)
 *     }
 * }
 */

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

function isSubPath(head: ListNode | null, root: TreeNode | null): boolean {
    const isCorrespond = (head, node) => {
        if (head === null) {
            return true;
        }
        if (node === null || head.val !== node.val) {
            return false;
        }
        return isCorrespond(head.next, node.left) || isCorrespond(head.next, node.right);
    }
    let ret = false;
    const traverse = node => {
        if (ret || node === null) {
            return;
        }
        if (isCorrespond(head, node)) {
            ret = true;
            return;
        }
        traverse(node.left);
        traverse(node.right);
    }
    traverse(root);
    return ret;
};

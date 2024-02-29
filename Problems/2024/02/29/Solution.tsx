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

function isEvenOddTree(root: TreeNode | null): boolean {
    let nodes = [root];
    let level = 0;
    while (nodes.length > 0) {
        if (level % 2 == 0) {
            for (let i = 0; i < nodes.length-1; i++) {
                if (nodes[i].val >= nodes[i+1].val) {
                    return false;
                }
            }
        } else {
            for (let i = 0; i < nodes.length-1; i++) {
                if (nodes[i].val <= nodes[i+1].val) {
                    return false;
                }
            }
        }
        let next = [];
        for (const node of nodes) {
            if (node.val % 2 === level % 2) {
                return false;
            }
            if (node.left !== null) {
                next.push(node.left);
            }
            if (node.right !== null) {
                next.push(node.right);
            }
        }
        nodes = next;
        level++;
    }
    return true;
};

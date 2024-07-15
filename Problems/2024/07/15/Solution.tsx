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

function createBinaryTree(descriptions: number[][]): TreeNode | null {
    const nodes = new Map();
    for (const [p, c, isLeft] of descriptions) {
        if (!nodes.has(p)) {
            nodes.set(p, [new TreeNode(p), 0]);
        }
        if (!nodes.has(c)) {
            nodes.set(c, [new TreeNode(c), 0]);
        }
        if (isLeft) {
            nodes.get(p)[0].left = nodes.get(c)[0];
        } else {
            nodes.get(p)[0].right = nodes.get(c)[0];
        }
        nodes.get(c)[1]++;
    }

    for (const [node, children] of nodes.values()) {
        if (children === 0) {
            return node;
        }
    }

    return null;
};

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

const graph: Map<number, Array<number>> = new Map();

function distanceK(root: TreeNode | null, target: TreeNode | null, k: number): number[] {
    constructGraph(root);
    let q: number[] = [target.val];
    const visited: Set<number> = new Set();
    for (let i = 0; i < k; i++) {
        const newQ: number[] = new Array();
        for (const cur of q) {
            visited.add(cur);
            for (const next of graph.get(cur)) {
                if (!visited.has(next)) {newQ.push(next);}
            }
        }
        q = newQ;
    }
    return q;
};

function constructGraph(root: TreeNode | null): void {
    if (root === null) {return;}
    graph.set(root.val, new Array());
    if (root.left !== null) {
        graph.get(root.val).push(root.left.val);
        constructGraph(root.left);
        graph.get(root.left.val).push(root.val);
    }
    if (root.right !== null) {
        graph.get(root.val).push(root.right.val);
        constructGraph(root.right);
        graph.get(root.right.val).push(root.val);
    }
};

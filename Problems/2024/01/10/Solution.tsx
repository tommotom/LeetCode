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

function amountOfTime(root: TreeNode | null, start: number): number {
    const graph = new Map();
    function toGraph(node: TreeNode | null): void {
        if (node === null) {
            return;
        }
        if (!graph.has(node.val)) {
            graph.set(node.val, []);
        }
        if (node.left !== null) {
            graph.set(node.left.val, [node.val]);
            graph.get(node.val).push(node.left.val);
            toGraph(node.left);
        }
        if (node.right !== null) {
            graph.set(node.right.val, [node.val]);
            graph.get(node.val).push(node.right.val);
            toGraph(node.right);
        }
    }
    toGraph(root);

    const memo = new Map();
    function depth(num: number): number {
        if (memo.has(num)) {
            return memo.get(num);
        }
        let ret = 0;
        for (const next of graph.get(num)) {
            graph.get(next).some(function(v, i){
                if (v==num) graph.get(next).splice(i,1);
            });
            ret = Math.max(ret, depth(next)+1);
        }
        memo.set(num, ret);
        return ret;
    }

    return depth(start);
};

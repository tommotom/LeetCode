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

function getDirections(root: TreeNode | null, startValue: number, destValue: number): string {
    const parents = new Map();
    let start = null, dest = null;
    const traverse = node => {
        if (node === null) {
            return;
        }
        if (node.val === startValue) {
            start = node;
        }
        if (node.val === destValue) {
            dest = node;
        }
        if (node.left !== null) {
            parents.set(node.left, node);
            traverse(node.left);
        }
        if (node.right !== null) {
            parents.set(node.right, node);
            traverse(node.right);
        }
    }
    traverse(root);

    let found = false;
    const visited = new Set();
    const dfs = (node, path) => {
        if (node === dest) {
            found = true;
            return path.join('');
        }
        if (visited.has(node)) {
            return;
        }
        visited.add(node);
        if (parents.has(node)) {
            path.push('U');
            const ret = dfs(parents.get(node), path);
            if (found) {
                return ret;
            }
            path.pop();
        }
        if (node.left !== null) {
            path.push('L');
            const ret = dfs(node.left, path);
            if (found) {
                return ret;
            }
            path.pop();
        }
        if (node.right !== null) {
            path.push('R');
            const ret = dfs(node.right, path);
            if (found) {
                return ret;
            }
            path.pop();
        }
    }

    return dfs(start, []);
};

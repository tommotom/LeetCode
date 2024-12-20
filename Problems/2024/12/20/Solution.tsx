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

function reverseOddLevels(root: TreeNode | null): TreeNode | null {
    let row = [root];
    let level = 0;
    while (row.length > 0) {
        if (level % 2 === 1) {
            let l = 0, r = row.length - 1;
            while (l < r) {
                const tmp = row[l].val;
                row[l].val = row[r].val;
                row[r].val = tmp;
                l++;
                r--;
            }
        }
        level++;
        const nextRow = [];
        for (const node of row) {
            if (node.left === null) {
                break;
            }
            nextRow.push(node.left);
            nextRow.push(node.right);
        }
        row = nextRow;
    };
    return root;
};

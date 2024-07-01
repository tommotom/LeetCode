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

function balanceBST(root: TreeNode | null): TreeNode | null {
    if (root === null) {
        return null;
    }

    const head = new TreeNode(0);
    head.right = root;
    let cur = head;
    while (cur.right !== null) {
        if (cur.right.left !== null) {
            rightRotate(cur, cur.right);
        } else {
            cur = cur.right;
        }
    }

    let count = 0;
    cur = head.right;
    while (cur !== null) {
        count++;
        cur = cur.right;
    }

    let m = Math.pow(2, Math.floor(Math.log2(count+1))) - 1;
    makeRotations(head, m);
    while (m > 1) {
        m = Math.floor(m/2);
        makeRotations(head, m);
    }

    return head.right;
};

function rightRotate(parent, node) {
    const tmp = node.left;
    node.left = tmp.right;
    tmp.right = node;
    parent.right = tmp;
}

function leftRotate(parent, node) {
    const tmp = node.right;
    node.right = tmp.left;
    tmp.left = node;
    parent.right = tmp;
}

function makeRotations(head, count) {
    let cur = head;
    for (let i = 0; i < count; i++) {
        console.log(cur);
        const tmp = cur.right;
        leftRotate(cur, tmp);
        cur = cur.right;
    }
}

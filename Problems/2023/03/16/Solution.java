/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {

    int[] inorder;
    int[] postorder;
    int p;

    public TreeNode buildTree(int[] inorder, int[] postorder) {
        this.inorder = inorder;
        this.postorder = postorder;
        this.p = postorder.length - 1;
        return helper(0, inorder.length);
    }

    private TreeNode helper(int l, int r) {
        if (p < 0) {
            return null;
        }

        int i = -1;
        for (int j = l; j < r; j++) {
            if (inorder[j] == postorder[p]) {
                i = j;
                break;
            }
        }

        if (i == -1) {
            return null;
        }

        TreeNode ret = new TreeNode(postorder[p]);
        p--;
        ret.right = helper(i+1, r);
        ret.left = helper(l, i);
        return ret;
    }
}

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

    private int ans = Integer.MAX_VALUE;

    public int minDiffInBST(TreeNode root) {
        if (root == null) {return 0;}
        if (root.left != null) {
            ans = Math.min(ans, root.val - max(root.left));
            minDiffInBST(root.left);
        }
        if (root.right != null) {
            ans = Math.min(ans, min(root.right)-root.val);
            minDiffInBST(root.right);
        }
        return ans;
    }

    private int min(TreeNode root) {
        return root.left == null ? root.val : min(root.left);
    }

    private int max(TreeNode root) {
        return root.right == null ? root.val : max(root.right);
    }
}

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
    public String tree2str(TreeNode root) {
        if (root == null) {return null;}
        String left = tree2str(root.left);
        String right = tree2str(root.right);
        if (left == null && right == null) {
            return String.valueOf(root.val);
        }
        if (left == null && right != null) {
            return root.val + "()(" + right + ")";
        }
        if (left != null && right == null) {
            return root.val + "(" + left + ")";
        }
        return root.val + "(" + left + ")" + "(" + right + ")";
    }
}

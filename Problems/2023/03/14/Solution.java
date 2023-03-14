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

    private int ans;

    public int sumNumbers(TreeNode root) {
        helper(root, 0);
        return ans;
    }

    private void helper(TreeNode node, int cur) {
        if (node == null) {
            return;
        }
        cur = cur * 10 + node.val;
        if (isLeaf(node)) {
            ans += cur;
        } else {
            helper(node.left, cur);
            helper(node.right, cur);
        }
    }

    private boolean isLeaf(TreeNode node) {
        return node != null && node.left == null && node.right == null;
    }
}

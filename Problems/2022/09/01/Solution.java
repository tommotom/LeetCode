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
    public int goodNodes(TreeNode root) {
        return helper(root, Integer.MIN_VALUE);
    }

    private int helper(TreeNode node, int max) {
        if (node == null) {return 0;}
        int ret = node.val >= max ? 1 : 0;
        max = Math.max(max, node.val);
        ret += helper(node.left, max);
        ret += helper(node.right, max);
        return ret;
    }
}

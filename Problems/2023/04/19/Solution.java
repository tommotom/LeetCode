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

    public int longestZigZag(TreeNode root) {
        helper(root);
        return ans;
    }
    private Pair<Integer, Integer> helper(TreeNode node) {
        if (node == null) {
            return new Pair(-1, -1);
        }
        Pair<Integer, Integer> left = helper(node.left);
        Pair<Integer, Integer> right = helper(node.right);
        int l = left.getValue()+1;
        int r = right.getKey()+1;
        ans = Math.max(ans, l);
        ans = Math.max(ans, r);
        return new Pair(l, r);
    }
}

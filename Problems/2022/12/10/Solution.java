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

    private final Map<TreeNode, Long> sum = new HashMap<>();
    private long ans;
    private long total;

    public int maxProduct(TreeNode root) {
        total = sumOf(root);
        helper(root);
        return (int)(ans%1000000007);
    }

    private void helper(TreeNode node) {
        if (node == null) {return;}
        long s = sumOf(node);
        ans = Math.max(ans, s*(total-s));
        helper(node.left);
        helper(node.right);
    }

    private long sumOf(TreeNode node) {
        if (node == null) {return 0;}
        if (!sum.containsKey(node)) {
            sum.put(node, node.val + sumOf(node.left) + sumOf(node.right));
        }
        return sum.get(node);
    }
}

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

    private final Map<TreeNode, Integer> lefts = new HashMap<>();
    private final Map<TreeNode, Integer> rights = new HashMap<>();
    private int ans = Integer.MIN_VALUE;

    public int maxPathSum(TreeNode root) {
        traverse(root);
        return ans;
    }

    private int traverse(TreeNode node) {
        if (node == null) {
            return 0;
        }
        if (!lefts.containsKey(node)) {
            lefts.put(node, traverse(node.left));
        }
        int left = lefts.get(node);
        if (!rights.containsKey(node)) {
            rights.put(node, traverse(node.right));
        }
        int right = rights.get(node);
        ans = Math.max(ans, Math.max(left, 0) + Math.max(right, 0) + node.val);
        int ret = Math.max(0, Math.max(left, right)) + node.val;
        return ret;
    }
}

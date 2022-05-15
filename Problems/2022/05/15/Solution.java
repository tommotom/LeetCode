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

  private int depth = 0;
  private int sum = 0;

  public int deepestLeavesSum(TreeNode root) {
    dfs(root, 0);
    return sum;
  }

  private void dfs(TreeNode node, int level) {
    if (node == null) {
      return;
    }
    if (level > depth) {
      depth = level;
      sum = 0;
    }
    dfs(node.left, level+1);
    dfs(node.right, level+1);
    if (level == depth) {
      sum += node.val;
    }
  }
}

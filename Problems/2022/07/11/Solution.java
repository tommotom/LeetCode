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
  public List<Integer> rightSideView(TreeNode root) {
    if (root == null) {
      return new ArrayList<>();
    }
    List<Integer> ans = new ArrayList<>();
    LinkedList<Integer> levels = new LinkedList<>();
    LinkedList<TreeNode> nodes = new LinkedList<>();
    levels.add(0);
    nodes.add(root);
    int level = -1;
    while (levels.size() > 0) {
      int l = levels.pollFirst();
      TreeNode n = nodes.pollFirst();
      level = Math.max(l, level);
      if (ans.size() == level) {
        ans.add(n.val);
      } else {
        ans.set(level, n.val);
      }
      if (n.left != null) {
        levels.addLast(l+1);
        nodes.addLast(n.left);
      }
      if (n.right != null) {
        levels.addLast(l+1);
        nodes.addLast(n.right);
      }
    }
    return ans;
  }
}

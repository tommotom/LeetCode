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
  public int kthSmallest(TreeNode root, int k) {
    Stack<TreeNode> stack = new Stack<>();
    TreeNode node = root;
    while (true) {
      if (node != null){
        stack.add(node);
        node = node.left;
      } else {
        node = stack.pop();
        k -= 1;
        if (k == 0) {
          return node.val;
        }
        node = node.right;
      }
    }
  }
}

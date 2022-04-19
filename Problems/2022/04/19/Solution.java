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

  private TreeNode first;
  private TreeNode second;
  private TreeNode prev;

  public void recoverTree(TreeNode root) {

    inorderTraversal(root);

    int tmp = first.val;
    first.val = second.val;
    second.val = tmp;
  }

  private void inorderTraversal(TreeNode root) {
    if (root == null) {
      return;
    }
    inorderTraversal(root.left);
    if (prev != null && prev.val > root.val) {
      if (first == null) {
        first = prev;
      }
      second = root;
    }
    prev = root;
    inorderTraversal(root.right);
  }
}

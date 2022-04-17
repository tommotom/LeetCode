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
  public TreeNode increasingBST(TreeNode root) {
    return align(root)[0];
  }

  private TreeNode[] align(TreeNode root) {
    TreeNode[] ret = {null, null};

    if (root == null) {
      return ret;
    }

    TreeNode[] left = align(root.left);
    TreeNode[] right = align(root.right);

    if (left[1] != null) {
      left[1].right = root;
    }

    root.left = null;
    root.right = right[0];

    ret[0] = left[0] != null ? left[0] : root;
    ret[1] = right[1] != null ? right[1] : root;

    return ret;
  }
}

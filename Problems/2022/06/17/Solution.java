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

  private int ans = 0;

  public int minCameraCover(TreeNode root) {
    monitorGrandChild(root);
    if (root.val == 0 || (root.left != null && root.left.val == 0) || (root.right != null && root.right.val == 0)) {
      ans++;
    }
    return ans;
  }

  private void tra(TreeNode node) {
    if (node == null) {
      return;
    }
    System.out.println(node.val);
    tra(node.left);
    tra(node.right);
  }

  private void monitorGrandChild(TreeNode node) {
    if (node == null) {
      return;
    }
    monitorGrandChild(node.left);
    monitorGrandChild(node.right);

    boolean left = isNeeded(node.left);
    boolean right = isNeeded(node.right);
    if (left) {
      ans++;
    }
    if (right) {
      ans++;
    }
    if (left || right) {
      if (node.val == 0) {
        node.val++;
      }
    }
  }

  private boolean isNeeded(TreeNode node) {
    if (node == null) {
      return false;
    }
    boolean isNeeded = false;
    if (node.left != null && node.left.val == 0) {
      isNeeded = true;
      node.left.val++;
    }
    if (node.right != null && node.right.val == 0) {
      isNeeded = true;
      node.right.val++;
    }
    if (isNeeded && node.val == 0) {
      node.val++;
    }
    return isNeeded;
  }
}

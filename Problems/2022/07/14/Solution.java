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

  private int[] preorder;
  private int[] inorder;
  private int i = 0;

  public TreeNode buildTree(int[] preorder, int[] inorder) {
    this.preorder = preorder;
    this.inorder = inorder;
    return helper(0, inorder.length);
  }

  private TreeNode helper(int l, int r) {
    if (i == preorder.length || l == r) {
      return null;
    }
    TreeNode node = new TreeNode(preorder[i]);
    int j = l;
    while (j < r) {
      if (inorder[j] == preorder[i]) {
        break;
      }
      j++;
    }
    i++;
    if (l < j) {
      node.left = helper(l, j);
    }
    if (j+1 < r) {
      node.right = helper(j+1, r);
    }
    return node;
  }
}

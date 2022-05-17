/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */

class Solution {
  public final TreeNode getTargetCopy(final TreeNode original, final TreeNode cloned, final TreeNode target) {
    Stack<TreeNode> st1 = new Stack<>(), st2 = new Stack<>();
    TreeNode node1 = original, node2 = cloned;
    while (true) {
      if (node1 != null) {
        st1.push(node1);
        node1 = node1.left;
        st2.push(node2);
        node2 = node2.left;
      } else {
        node1 = st1.pop();
        node2 = st2.pop();
        if (node1 == target) {
          return node2;
        }
        node1 = node1.right;
        node2 = node2.right;
      }
    }
  }
}

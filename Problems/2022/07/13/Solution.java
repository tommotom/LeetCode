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
  public List<List<Integer>> levelOrder(TreeNode root) {
    List<List<Integer>> ans = new ArrayList<>();
    if (root == null) {
      return ans;
    }

    LinkedList<TreeNode> cur = new LinkedList<>();
    cur.add(root);

    while (cur.size() > 0) {
      LinkedList<TreeNode> next = new LinkedList<>();
      ArrayList<Integer> level = new ArrayList<>();
      int size = cur.size();
      for (int i = 0; i < size; i++) {
        TreeNode tmp = cur.pollFirst();
        level.add(tmp.val);
        if (tmp.left != null) {
          next.addLast(tmp.left);
        }
        if (tmp.right != null) {
          next.addLast(tmp.right);
        }
      }
      ans.add(level);
      cur = next;
    }

    return ans;
  }
}

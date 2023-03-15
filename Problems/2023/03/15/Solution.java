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
    public boolean isCompleteTree(TreeNode root) {
        LinkedList<TreeNode> cur = new LinkedList<>();
        cur.add(root);
        boolean foundNull = false;
        while (cur.size() > 0) {
            LinkedList<TreeNode> next = new LinkedList<>();
            while (cur.size() > 0) {
                TreeNode node = cur.poll();
                if (node.left == null) {
                    foundNull = true;
                } else if (foundNull) {
                    return false;
                } else {
                    next.add(node.left);
                }
                if (node.right == null) {
                    foundNull = true;
                } else if (foundNull) {
                    return false;
                } else {
                    next.add(node.right);
                }
            }
            cur = next;
        }
        return true;
    }
}

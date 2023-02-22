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
    public List<List<Integer>> zigzagLevelOrder(TreeNode root) {
        List<List<Integer>> ans = new ArrayList<>();
        if (root == null) {
            return ans;
        }

        LinkedList<TreeNode> q = new LinkedList<>();
        q.add(root);
        boolean rev = false;
        while (q.size() > 0) {
            LinkedList<TreeNode> next = new LinkedList<>();
            List<Integer> row = new ArrayList<>();
            while (q.size() > 0) {
                TreeNode node = q.poll();
                row.add(node.val);
                if (node.left != null) {
                    next.add(node.left);
                }
                if (node.right != null) {
                    next.add(node.right);
                }
            }
            q = next;
            if (rev) {
                Collections.reverse(row);
                rev = false;
            } else {
                rev = true;
            }
            ans.add(row);
        }

        return ans;
    }
}

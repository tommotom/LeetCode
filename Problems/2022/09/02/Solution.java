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
    public List<Double> averageOfLevels(TreeNode root) {
        LinkedList<TreeNode> cur = new LinkedList<>();
        cur.add(root);
        List<Double> ans = new ArrayList<>();
        while (cur.size() > 0) {
            LinkedList<TreeNode> next = new LinkedList<>();
            long sum = 0;
            int count = cur.size();
            for (int i = 0; i < count; i++) {
                TreeNode node = cur.poll();
                sum += node.val;
                if (node.left != null) {
                    next.add(node.left);
                }
                if (node.right != null) {
                    next.add(node.right);
                }
            }
            ans.add((double)sum/count);
            cur = next;
        }
        return ans;
    }
}

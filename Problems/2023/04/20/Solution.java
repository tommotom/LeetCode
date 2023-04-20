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

    public int widthOfBinaryTree(TreeNode root) {
        int ans = 0;

        List<Pair<TreeNode, Integer>> row = new ArrayList<>();
        row.add(new Pair(root, 0));

        while (!row.isEmpty()) {
            List<Pair<TreeNode, Integer>> next = new ArrayList<>();
            int min = row.get(0).getValue();
            int max = min;
            for (Pair<TreeNode, Integer> r : row) {
                max = r.getValue();
                TreeNode node = r.getKey();
                if (node.left != null) {
                    next.add(new Pair(node.left, r.getValue()*2));
                }
                if (node.right != null) {
                    next.add(new Pair(node.right, r.getValue()*2+1));
                }
            }
            row = next;
            ans = Math.max(ans, max - min + 1);
        }
        return ans;
    }
}

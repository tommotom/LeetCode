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

    int ans;
    int depth;
    boolean done;

    public int countNodes(TreeNode root) {
        if (root == null) {return 0;}

        TreeNode node = root;
        while (node != null) {
            node = node.left;
            depth++;
        }
        ans = (int) Math.pow(2, depth) - 1;

        subtract(root, 1);

        return ans;
    }

    private void subtract(TreeNode node, int cur) {
        if (done) {return;}
        if (cur == depth) {
            if (node == null) {
                ans--;
            } else {
                done = true;
            }
            return;
        }
        subtract(node.right, cur+1);
        subtract(node.left, cur+1);
    }
}

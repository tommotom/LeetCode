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
    public void flatten(TreeNode root) {
        while (root != null) {
            if (root.left != null) {
                TreeNode right = root.right;
                TreeNode predecessor = root.left;
                while(predecessor.right != null) {
                    predecessor = predecessor.right;
                }
                predecessor.right = right;
                root.right = root.left;
                root.left = null;
            }
            root = root.right;
        }
    }
}

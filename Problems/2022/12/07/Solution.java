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
    public int rangeSumBST(TreeNode root, int low, int high) {
        if (root == null) {return 0;}
        int ret = 0;
        if (low <= root.val && root.val <= high) {ret += root.val;}
        ret += rangeSumBST(root.left, low, high);
        ret += rangeSumBST(root.right, low, high);
        return ret;
    }
}

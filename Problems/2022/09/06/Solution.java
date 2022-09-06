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

    Map<TreeNode, Boolean> isContainsOne = new HashMap<>();

    public TreeNode pruneTree(TreeNode root) {
        if (root == null) {return root;}
        pruneTree(root.left);
        pruneTree(root.right);
        root.left = isContainsOne(root.left) ? root.left : null;
        root.right = isContainsOne(root.right) ? root.right : null;
        return isContainsOne(root) ? root : null;
    }

    private boolean isContainsOne(TreeNode node) {
        if (node == null) {return false;}
        if (isContainsOne.containsKey(node)) {
            return isContainsOne.get(node);
        }
        boolean ret = node.val == 1 || isContainsOne(node.left) || isContainsOne(node.right);
        isContainsOne.put(node, ret);
        return ret;
    }
}

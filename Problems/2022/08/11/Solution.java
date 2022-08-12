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

    Map<TreeNode, Integer> maxs = new HashMap<>();
    Map<TreeNode, Integer> mins = new HashMap<>();

    public boolean isValidBST(TreeNode root) {
        if (root == null) {return true;}
        if (!isValidBST(root.left)) {return false;}
        if (!isValidBST(root.right)) {return false;}
        if (root.left != null && max(root.left) >= root.val) {return false;}
        if (root.right != null && min(root.right) <= root.val) {return false;}
        return true;
    }

    public int min(TreeNode root) {
        if (root == null) {return Integer.MAX_VALUE;}
        if (mins.containsKey(root)) {return mins.get(root);}
        int ret = root.val;
        ret = Math.min(ret, min(root.left));
        ret = Math.min(ret, min(root.right));
        mins.put(root, ret);
        return ret;
    }

    public int max(TreeNode root) {
        if (root == null) {return Integer.MIN_VALUE;}
        if (maxs.containsKey(root)) {return maxs.get(root);}
        int ret = root.val;
        ret = Math.max(ret, max(root.left));
        ret = Math.max(ret, max(root.right));
        maxs.put(root, ret);
        return ret;
    }
}

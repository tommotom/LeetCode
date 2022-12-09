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

    private final Map<TreeNode, Integer> maxs = new HashMap<>();
    private final Map<TreeNode, Integer> mins = new HashMap<>();

    public int maxAncestorDiff(TreeNode root) {
        int ret = 0;
        if (root == null) {
            return ret;
        }
        ret = Math.max(ret, maxAncestorDiff(root.left));
        ret = Math.max(ret, maxAncestorDiff(root.right));
        ret = Math.max(ret, max(root) - root.val);
        ret = Math.max(ret, root.val - min(root));
        return ret;
    }

    private int max(TreeNode root) {
        if (!maxs.containsKey(root)) {
            int val = root.val;
            if (root.left != null) {
                val = Math.max(val, max(root.left));
            }
            if (root.right != null) {
                val = Math.max(val, max(root.right));
            }
            maxs.put(root, val);
        }
        return maxs.get(root);
    }

    private int min(TreeNode root) {
        if (!mins.containsKey(root)) {
            int val = root.val;
            if (root.left != null) {
                val = Math.min(val, min(root.left));
            }
            if (root.right != null) {
                val = Math.min(val, min(root.right));
            }
            mins.put(root, val);
        }
        return mins.get(root);
    }
}

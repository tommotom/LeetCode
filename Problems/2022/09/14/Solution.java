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

    private int ans;
    private Map<Integer, Integer> counter = new HashMap<>();

    public int pseudoPalindromicPaths (TreeNode root) {
        helper(root);
        return ans;
    }

    private void helper(TreeNode node) {
        if (node == null) {
            return;
        }
        counter.put(node.val, counter.getOrDefault(node.val, 0) + 1);
        if (isLeaf(node)) {
            count();
        } else {
            helper(node.left);
            helper(node.right);
        }
        counter.put(node.val, counter.get(node.val) - 1);
    }

    private void count() {
        int odd = 0;
        for (int key : counter.keySet()) {
            if (counter.get(key) % 2 == 1) {
                odd++;
            }
        }
        if (odd < 2) {
            ans++;
        }
    }

    private boolean isLeaf(TreeNode node) {
        if (node == null) {return false;}
        return node.left == null && node.right == null;
    }
}

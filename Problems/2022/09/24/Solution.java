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

    private List<List<Integer>> ans = new ArrayList<>();
    private int target;

    public List<List<Integer>> pathSum(TreeNode root, int targetSum) {
        target = targetSum;
        helper(root, 0, new LinkedList<>());
        return ans;
    }

    private void helper(TreeNode node, int sum, LinkedList<Integer> path) {
        if(node==null){
            return;
        }
        sum += node.val;
        path.add(node.val);
        if(isLeaf(node)) {
            if(sum == target) {
                ans.add(new LinkedList<>(path));
            }
        } else {
            helper(node.left, sum, path);
            helper(node.right, sum, path);
        }
        sum -= node.val;
        path.pollLast();
    }

    private boolean isLeaf(TreeNode node) {
        return node != null && node.left ==null && node.right == null;
    }
}

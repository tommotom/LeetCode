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

    final Map<String, Integer> counter = new HashMap<>();
    final Map<String, TreeNode> nodes = new HashMap<>();

    public List<TreeNode> findDuplicateSubtrees(TreeNode root) {
        serialize(root);
        List<TreeNode> ans = new ArrayList<>();
        for (String key : nodes.keySet()) {
            if (counter.get(key) > 1) {
                ans.add(nodes.get(key));
            }
        }
        return ans;
    }

    private void serialize(TreeNode node) {
        if (node == null) {
            return;
        }
        serialize(node.left);
        serialize(node.right);

        String key = toString(node, new StringBuilder()).toString();
        counter.put(key, counter.getOrDefault(key, 0) + 1);
        nodes.putIfAbsent(key, node);
    }

    private StringBuilder toString(TreeNode node, StringBuilder sb) {
        if (node == null) {
            sb.append('#');
        } else {
            sb.append(node.val);
            sb.append(',');
            toString(node.left, sb);
            toString(node.right, sb);
        }
        return sb;
    }
}

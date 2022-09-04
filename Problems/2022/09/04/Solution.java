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
    PriorityQueue<MyNode> organizer = new PriorityQueue<>();

    public List<List<Integer>> verticalTraversal(TreeNode root) {
        dfs(0, 0, root);
        List<List<Integer>> ans = new ArrayList<>();
        int col = Integer.MIN_VALUE;
        while (organizer.size() > 0) {
            MyNode node = organizer.poll();
            if (node.col != col) {
                ans.add(new ArrayList<>());
                col = node.col;
            }
            ans.get(ans.size()-1).add(node.val);
        }
        return ans;
    }

    public void dfs(int row, int col, TreeNode node) {
        if (node == null) {return;}
        MyNode mynode = new MyNode(row, col, node.val);
        organizer.add(mynode);
        dfs(row+1, col-1, node.left);
        dfs(row+1, col+1, node.right);
    }
}

class MyNode implements Comparable<MyNode> {
    int row;
    int col;
    int val;

    public MyNode(int row, int col, int val) {
        this.row = row;
        this.col = col;
        this.val = val;
    }

    @Override
    public int compareTo(MyNode another) {
        if (this.col == another.col) {
            if (this.row == another.row) {
                return Integer.compare(this.val, another.val);
            }
            return Integer.compare(this.row, another.row);
        }
        return Integer.compare(this.col, another.col);
    }
}

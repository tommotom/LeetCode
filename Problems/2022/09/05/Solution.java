/*
// Definition for a Node.
class Node {
    public int val;
    public List<Node> children;

    public Node() {}

    public Node(int _val) {
        val = _val;
    }

    public Node(int _val, List<Node> _children) {
        val = _val;
        children = _children;
    }
};
*/

class Solution {
    public List<List<Integer>> levelOrder(Node root) {
        List<List<Integer>> ans = new ArrayList<>();
        if (root == null) {return ans;}

        LinkedList<Node> cur = new LinkedList<>();
        cur.add(root);
        while (cur.size() > 0) {
            List<Integer> vals = new ArrayList<>();
            LinkedList<Node> next = new LinkedList<>();
            while (cur.size() > 0) {
                Node node = cur.poll();
                vals.add(node.val);
                for (Node n : node.children) {
                    next.add(n);
                }
            }
            ans.add(vals);
            cur = next;
        }
        return ans;
    }
}

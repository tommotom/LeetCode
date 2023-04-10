/*
// Definition for a Node.
class Node {
    public int val;
    public List<Node> neighbors;
    public Node() {
        val = 0;
        neighbors = new ArrayList<Node>();
    }
    public Node(int _val) {
        val = _val;
        neighbors = new ArrayList<Node>();
    }
    public Node(int _val, ArrayList<Node> _neighbors) {
        val = _val;
        neighbors = _neighbors;
    }
}
*/

class Solution {

    private final Map<Integer, Node> nodes = new HashMap<>();

    public Node cloneGraph(Node node) {
        if (node == null) {
            return null;
        }
        if (nodes.containsKey(node.val)) {
            return nodes.get(node.val);
        }
        Node copy = new Node(node.val);
        nodes.put(node.val, copy);
        for (Node next : node.neighbors) {
            copy.neighbors.add(cloneGraph(next));
        }
        return copy;
    }
}

/*
// Definition for a Node.
class Node {
    int val;
    Node next;
    Node random;

    public Node(int val) {
        this.val = val;
        this.next = null;
        this.random = null;
    }
}
*/

class Solution {
  public Node copyRandomList(Node head) {
    Map<Node, Integer> nodeToOrder = new HashMap<>();
    Map<Integer, Node> orderToNode = new HashMap<>();

    Node node = head;
    Node dummyHead = new Node(0);
    Node copy = dummyHead;
    Integer order = 0;
    while (node != null) {
      copy.next = new Node(node.val);
      copy = copy.next;
      orderToNode.put(order, copy);

      nodeToOrder.put(node, order);
      node = node.next;

      order++;
    }

    node = head;
    copy = dummyHead.next;
    while (node != null) {
      if (node.random != null) {
        copy.random = orderToNode.get(nodeToOrder.get(node.random));
      }
      node = node.next;
      copy = copy.next;
    }

    return dummyHead.next;
  }
}
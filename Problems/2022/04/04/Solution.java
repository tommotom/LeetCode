/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
  public ListNode swapNodes(ListNode head, int k) {
    int len = length(head);

    ListNode dummy = new ListNode();
    dummy.next = head;

    ListNode a = dummy;
    for (int i = k; i > 1; i--) {
      a = a.next;
    }

    ListNode b = dummy;
    for (int i = len-k; i > 0; i--) {
      b = b.next;
    }

    swap(a, b);

    return dummy.next;
  }

  private int length(ListNode head) {
    ListNode tmp = head;
    int ret = 0;
    while (tmp != null) {
      ret++;
      tmp = tmp.next;
    }
    return ret;
  }

  private void swap(ListNode prev1, ListNode prev2) {
    if (prev1.next == prev2) {
      prev1.next = prev2.next;
      prev2.next = prev2.next.next;
      prev1.next.next = prev2;
      return;
    }
    if (prev2.next == prev1) {
      prev2.next = prev1.next;
      prev1.next = prev1.next.next;
      prev2.next.next = prev1;
      return;
    }

    ListNode node1 = prev1.next;
    ListNode node2 = prev2.next;
    ListNode next1 = node1.next;
    ListNode next2 = node2.next;
    prev1.next = node2;
    node2.next = next1;
    prev2.next = node1;
    node1.next = next2;
  }
}

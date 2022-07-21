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
  public ListNode reverseBetween(ListNode head, int left, int right) {
    ListNode dummy = new ListNode(0, head);
    ListNode node = dummy;
    for (int i = 1; i < left; i++) {
      node = node.next;
    }
    node.next = reverse(node.next, right-left);
    return dummy.next;
  }

  private ListNode reverse(ListNode head, int length) {
    ListNode dummy = new ListNode(0, head);
    ListNode tail = head;
    for (int i = 0; i < length; i++) {
      ListNode curHead = dummy.next;
      ListNode nextHead = tail.next;
      tail.next = tail.next.next;
      nextHead.next = curHead;
      dummy.next = nextHead;
    }
    return dummy.next;
  }
}

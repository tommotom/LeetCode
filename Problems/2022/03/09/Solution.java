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
  public ListNode deleteDuplicates(ListNode head) {
    ListNode dummy = new ListNode(0, head);
    ListNode node = dummy;

    while (node != null && node.next != null && node.next.next != null) {
      if (node.next.val == node.next.next.val) {
        ListNode tmp = node.next;
        while (tmp.next != null && tmp.val == tmp.next.val) {
          tmp = tmp.next;
        }
        node.next = tmp.next;
      } else {
        node = node.next;
      }
    }

    return dummy.next;
  }
}

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
  public ListNode partition(ListNode head, int x) {
    ListNode lessHead = new ListNode(0);
    ListNode moreHead = new ListNode(0);
    ListNode lessTail = lessHead;
    ListNode moreTail = moreHead;
    while (head != null) {
      ListNode tmp = head;
      head = head.next;
      tmp.next = null;
      if (tmp.val < x) {
        lessTail.next = tmp;
        lessTail = lessTail.next;
      } else {
        moreTail.next = tmp;
        moreTail = moreTail.next;
      }
    }
    lessTail.next = moreHead.next;
    return lessHead.next;
  }
}

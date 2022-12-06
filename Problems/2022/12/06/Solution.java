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
    public ListNode oddEvenList(ListNode head) {
        ListNode oddhead = new ListNode(), evenhead = new ListNode();
        ListNode oddtail = oddhead, eventail = evenhead;
        int count = 0;
        while (head != null) {
            count++;
            if (count % 2 == 1) {
                oddtail.next = head;
                oddtail = oddtail.next;
                head = head.next;
                oddtail.next = null;
            } else {
                eventail.next = head;
                eventail = eventail.next;
                head = head.next;
                eventail.next = null;
            }
        }
        oddtail.next = evenhead.next;
        return oddhead.next;
    }
}

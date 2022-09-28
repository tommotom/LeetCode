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
    public ListNode removeNthFromEnd(ListNode head, int n) {
        int target = length(head) - n + 1;
        if (target == 1) {
            return head.next;
        }

        ListNode prev = head;
        for (int i = 2; i < target; i++) {
            prev = prev.next;
        }
        prev.next = prev.next.next;
        return head;
    }

    private int length(ListNode head) {
        ListNode node = head;
        int ret = 0;
        while (node != null) {
            ret++;
            node = node.next;
        }
        return ret;
    }
}

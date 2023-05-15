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
        int len = len(head);
        if (k > len / 2) {
            k = len - k + 1;
        }

        ListNode node = head;
        for (int i = 1; i < k; i++) {
            node = node.next;
        }
        ListNode a = node;
        for (int i = k; i <= len - k; i++) {
            node = node.next;
        }

        int tmp = a.val;
        a.val = node.val;
        node.val = tmp;

        return head;
    }

    private int len(ListNode head) {
        int len = 0;
        while (head != null) {
            head = head.next;
            len++;
        }
        return len;
    }
}

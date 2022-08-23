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
    public boolean isPalindrome(ListNode head) {
        int length = 0;
        ListNode node = head;
        while (node != null) {
            node = node.next;
            length++;
        }
        if (length == 1) {return true;}

        Stack<Integer> st = new Stack<>();
        ListNode dummy = new ListNode(0, head);
        node = head;
        for (int i = 0; i < length/2-1; i++) {
            ListNode tmp = node.next;
            node.next = tmp.next;
            tmp.next = dummy.next;
            dummy.next = tmp;
        }

        node = node.next;
        if (length % 2 == 1) {
            node = node.next;
        }
        ListNode slow = dummy.next;
        while (node != null) {
            if (node.val != slow.val) {return false;}
            node = node.next;
            slow = slow.next;
        }
        return true;
    }
}

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
    public int pairSum(ListNode head) {
        int len = 0;
        ListNode node = head;
        while (node != null) {
            node = node.next;
            len++;
        }

        int n = len / 2;
        int[] pair = new int[n];
        node = head;
        for (int i = 0; i < n; i++) {
            pair[i] += node.val;
            node = node.next;
        }
        for (int i = 0; i < n; i++) {
            pair[n-i-1] += node.val;
            node = node.next;
        }

        return Arrays.stream(pair).max().getAsInt();
    }
}

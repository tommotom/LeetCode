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
    public ListNode mergeKLists(ListNode[] lists) {
        if (lists.length == 0) {
            return null;
        }
        while (lists.length > 1) {
            int n = lists.length;
            int m = n/2 + n%2;
            ListNode[] merged = new ListNode[m];
            for (int i = 0; i < m; i++) {
                merged[i] = merge(lists[i*2], i*2+1 == n ? null : lists[i*2+1]);
            }
            lists = merged;
        }
        return lists[0];
    }

    private ListNode merge(ListNode a, ListNode b) {
        if (b == null) {
            return a;
        }
        ListNode head = new ListNode();
        ListNode cur = head;
        while (a != null && b != null) {
            if (a.val < b.val) {
                cur.next = a;
                cur = cur.next;
                ListNode tmp = a.next;
                a.next = null;
                a = tmp;
            } else {
                cur.next = b;
                cur = cur.next;
                ListNode tmp = b.next;
                b.next = null;
                b = tmp;
            }
        }
        if (a != null) {
            cur.next = a;
        }
        if (b != null) {
            cur.next = b;
        }
        return head.next;
    }
}

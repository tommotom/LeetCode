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

    int[] vals;
    Random rand = new Random();

    public Solution(ListNode head) {
        int len = 0;
        ListNode node = head;
        while(node != null) {
            node = node.next;
            len++;
        }

        vals = new int[len];
        node = head;
        for (int i = 0; i < len; i++) {
            vals[i] = node.val;
            node = node.next;
        }
    }

    public int getRandom() {
        return vals[rand.nextInt(vals.length)];
    }
}

/**
 * Your Solution object will be instantiated and called as such:
 * Solution obj = new Solution(head);
 * int param_1 = obj.getRandom();
 */

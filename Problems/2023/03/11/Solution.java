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
/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {

    ListNode cur;

    public TreeNode sortedListToBST(ListNode head) {
        int len = 0;
        ListNode node = head;
        while (node != null) {
            node = node.next;
            len++;
        }

        cur = head;

        return helper(0, len);
    }

    TreeNode helper(int l, int r) {
        if (l == r) {
            return null;
        }

        int m = l + (r - l) / 2;

        TreeNode left = helper(l, m);
        TreeNode node = new TreeNode(cur.val);
        cur = cur.next;
        TreeNode right = helper(m+1, r);
        node.left = left;
        node.right = right;

        return node;
    }
}

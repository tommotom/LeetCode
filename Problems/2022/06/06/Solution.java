/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) {
 *         val = x;
 *         next = null;
 *     }
 * }
 */
public class Solution {
  public ListNode getIntersectionNode(ListNode headA, ListNode headB) {
    ListNode tmp = headA;
    while (tmp != null) {
      tmp.val *= -1;
      tmp = tmp.next;
    }

    tmp = headB;
    ListNode ans = null;
    while (tmp != null) {
      tmp.val *= -1;
      if (ans == null && tmp.val > 0) {
        ans = tmp;
      }
      tmp = tmp.next;
    }

    while (headA != null) {
      headA.val *= -1;
      headA = headA.next;
    }

    while (headB != null) {
      headB.val *= -1;
      headB = headB.next;
    }

    return ans;
  }
}

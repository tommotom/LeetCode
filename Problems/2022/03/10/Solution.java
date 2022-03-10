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
  public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
    if (length(l1) < length(l2)) {
      ListNode tmp = l1;
      l1 = l2;
      l2 = tmp;
    }

    int carry = 0;
    ListNode n1 = l1;
    ListNode n2 = l2;
    while (n1 != null && n2 != null) {
      int newVal = n1.val + n2.val + carry;
      carry = newVal > 9 ? 1 : 0;
      n1.val = newVal % 10;
      n1 = n1.next;
      n2 = n2.next;
    }

    while (carry > 0 && n1 != null) {
      int newVal = n1.val + carry;
      carry = newVal > 9 ? 1 : 0;
      n1.val = newVal % 10;
      n1 = n1.next;
    }

    if (carry > 0) {
      return addToTail(l1, carry);
    }

    return l1;
  }

  private int length(ListNode l) {
    int length = 0;
    ListNode tmp = l;
    while (tmp != null) {
      length++;
      tmp = tmp.next;
    }
    return length;
  }

  private ListNode addToTail(ListNode l, int val) {
    if (l == null) {
      return new ListNode(val);
    }

    ListNode tmp = l;
    while (tmp != null && tmp.next != null) {
      tmp = tmp.next;
    }
    tmp.next = new ListNode(val);
    return l;
  }
}
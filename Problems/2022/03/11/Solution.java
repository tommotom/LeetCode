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
  public ListNode rotateRight(ListNode head, int k) {
    if (head == null) {
      return head;
    }

    int length = length(head);

    k %= length;
    if (k == 0) {
      return head;
    }

    ListNode newHead = head;
    for (int i=0; i<length-k-1; i++) {
      newHead = newHead.next;
    }

    ListNode tmp = newHead;
    newHead = newHead.next;
    tmp.next = null;

    ListNode tail = newHead;
    while (tail.next != null) {
      tail = tail.next;
    }

    tail.next = head;

    return newHead;
  }

  private int length(ListNode head) {
    ListNode tmp = head;
    int length = 0;
    while (tmp != null) {
      tmp = tmp.next;
      length++;
    }
    return length;
  }
}

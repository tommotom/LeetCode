/**
 * Definition for singly-linked list.
 * class ListNode {
 *     val: number
 *     next: ListNode | null
 *     constructor(val?: number, next?: ListNode | null) {
 *         this.val = (val===undefined ? 0 : val)
 *         this.next = (next===undefined ? null : next)
 *     }
 * }
 */

function addTwoNumbers(l1: ListNode | null, l2: ListNode | null): ListNode | null {
    l1 = reverse(l1);
    l2 = reverse(l2);
    const head = new ListNode();
    let cur = head;
    let carry = 0;
    while (l1 !== null && l2 !== null) {
        const val = l1.val + l2.val + carry;
        cur.next = new ListNode(val % 10);
        carry = Math.floor(val / 10);
        cur = cur.next;
        l1 = l1.next;
        l2 = l2.next;
    }
    while (l1 !== null) {
        const val = l1.val + carry;
        cur.next = new ListNode(val % 10);
        carry = Math.floor(val / 10);
        cur = cur.next;
        l1 = l1.next;
    }
    while (l2 !== null) {
        const val = l2.val + carry;
        cur.next = new ListNode(val % 10);
        carry = Math.floor(val / 10);
        cur = cur.next;
        l2 = l2.next;
    }
    if (carry > 0) {
        cur.next = new ListNode(carry);
    }
    return reverse(head.next);
};

function reverse(l: ListNode | null): ListNode {
    if (l === null) {return l;}

    let head: ListNode = l;
    while (l.next !== null) {
        const tmp: ListNode = l.next;
        l.next = tmp.next;
        tmp.next = head;
        head = tmp;
    }
    return head;
}

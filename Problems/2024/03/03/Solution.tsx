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

function removeNthFromEnd(head: ListNode | null, n: number): ListNode | null {
    let len = 0;
    let node = head;
    while (node !== null) {
        len++;
        node = node.next;
    }

    if (n === len) {
        return head.next;
    }
    node = head;
    for (let i = 1; i < len-n; i++) {
        node = node.next;
    }
    node.next = node.next !== null ? node.next.next : null;

    return head;
};

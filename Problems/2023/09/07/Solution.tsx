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

function reverseBetween(head: ListNode | null, left: number, right: number): ListNode | null {
    function reverse(head: ListNode): ListNode {
        let node = head.next;
        head.next = null;
        while (node !== null) {
            const tmp = node.next;
            node.next = head;
            head = node;
            node = tmp;
        }
        return head;
    }

    let tail = head;
    for (let i = 0; i < right-1; i++) {
        tail = tail.next;
    }
    const tmp = tail.next;
    tail.next = null;
    tail = tmp;

    let node = head;
    if (left === 1) {
        head = reverse(head);
    } else {
        for (let i = 0; i < left-2; i++) {
            node = node.next;
        }
        node.next = reverse(node.next);
    }
    while (node.next !== null) {
        node = node.next;
    }
    node.next = tail;

    return head;
};

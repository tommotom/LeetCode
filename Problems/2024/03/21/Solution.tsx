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

function reverseList(head: ListNode | null): ListNode | null {
    const dummy = new ListNode(0, head);
    while (head !== null && head.next !== null) {
        const tmp = head.next;
        head.next = tmp.next;
        tmp.next = dummy.next;
        dummy.next = tmp;
    }
    return dummy.next;
};

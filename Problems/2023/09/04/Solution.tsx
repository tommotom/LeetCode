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

function hasCycle(head: ListNode | null): boolean {
    let l = head, r = head;
    while (r !== null && r.next !== null && r.next.next !== null) {
        l = l.next;
        r = r.next.next;
        if (r === l) {
            return true;
        }
    }
    return false;
};

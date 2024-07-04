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

function mergeNodes(head: ListNode | null): ListNode | null {
    let node = head.next;
    head = node;
    while (node !== null) {
        while (node.next.val !== 0) {
            node.val += node.next.val;
            node.next = node.next.next;
        }
        node.next = node.next.next;
        node = node.next;
    }
    return head;
};

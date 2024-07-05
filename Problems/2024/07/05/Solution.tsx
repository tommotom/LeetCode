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

function nodesBetweenCriticalPoints(head: ListNode | null): number[] {
    const isMaxima = node => node.val < node.next.val && node.next.val > node.next.next.val;
    const isMinima = node => node.val > node.next.val && node.next.val < node.next.next.val;
    const isCritical = node => isMaxima(node) || isMinima(node);

    let first = -1, last = -1, min = Number.MAX_SAFE_INTEGER, i = 0;
    let node = head;
    while (node !== null && node.next !== null && node.next.next !== null) {
        if (isCritical(node)) {
            if (first === -1) {
                first = i;
            }
            if (last !== -1) {
                min = Math.min(min, i - last)
            }
            last = i;
        }
        node = node.next;
        i++;
    }

    return min === Number.MAX_SAFE_INTEGER
        ? [-1, -1]
        : [min, last - first];
};

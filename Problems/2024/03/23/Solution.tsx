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

/**
 Do not return anything, modify head in-place instead.
 */
function reorderList(head: ListNode | null): void {
    let length = 0, node = head;
    while (node !== null) {
        length++;
        node = node.next;
    }
    let head2 = head;
    for (let i = 1; i < Math.ceil(length/2); i++) {
        head2 = head2.next;
    }
    node = head2.next;
    while (node !== null && node.next !== null) {
        const tmp = node.next;
        node.next = tmp.next;
        tmp.next = head2.next;
        head2.next = tmp;
    }
    const tmp = head2.next;
    head2.next = null;
    head2 = tmp;

    node = head;
    while (head2 !== null) {
        const tmp = head2.next;
        head2.next = node.next;
        node.next = head2;
        node = node.next.next;
        head2 = tmp;
    }
};

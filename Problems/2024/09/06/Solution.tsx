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

function modifiedList(nums: number[], head: ListNode | null): ListNode | null {
    const set = new Set(nums);
    const dummy = new ListNode(0, head);
    let node = dummy;
    while (node.next) {
        if (set.has(node.next.val)) {
            node.next = node.next.next;
        } else {
            node = node.next;
        }
    }
    return dummy.next;
};

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

function doubleIt(head: ListNode | null): ListNode | null {
    const helper = node => {
        if (node === null) {
            return {next: null, carry: 0};
        }
        const {next, carry} = helper(node.next);
        node.next = next;
        node.val = node.val * 2 + carry;
        const tmp = Math.floor(node.val / 10);
        node.val %= 10;
        return {next: node, carry: tmp};
    }
    const {next, carry} = helper(head);
    return carry > 0 ? new ListNode(carry, next) : next;
};

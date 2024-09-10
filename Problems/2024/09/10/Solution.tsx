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

function insertGreatestCommonDivisors(head: ListNode | null): ListNode | null {
    const gcd = (a, b) => {
        if (b > a) {
            return gcd(b, a);
        }
        if (b === 0) {
            return a;
        }
        return gcd(b, a % b);
    }
    let node = head;
    while (node && node.next) {
        node.next = new ListNode(gcd(node.val, node.next.val), node.next);
        node = node.next.next;
    }
    return head;
};

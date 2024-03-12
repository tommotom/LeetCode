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

function removeZeroSumSublists(head: ListNode | null): ListNode | null {
    const dummy = new ListNode(0, head);
    let fast = head;
    let sum = 0;
    while (fast !== null) {
        sum += fast.val;
        let tmp = sum;
        let slow = dummy;
        while (slow !== fast) {
            if (tmp === 0) {
                while (slow.next !== fast) {
                    slow.next = slow.next.next;
                }
                slow.next = slow.next.next;
                break;
            }
            slow = slow.next;
            tmp -= slow.val;
        }
        fast = slow.next;
    }
    return dummy.next;
};

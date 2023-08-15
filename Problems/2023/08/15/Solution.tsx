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

function partition(head: ListNode | null, x: number): ListNode | null {
    let less = new ListNode(), more = new ListNode();
    const lessHead = less, moreHead = more;
    while (head !== null) {
        const tmp = head;
        head = head.next;
        tmp.next = null;
        if (tmp.val < x) {
            less.next = tmp;
            less = less.next;
        } else {
            more.next = tmp;
            more = more.next;
        }
    }
    less.next = moreHead.next;
    return lessHead.next;
};

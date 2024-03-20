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

function mergeInBetween(list1: ListNode | null, a: number, b: number, list2: ListNode | null): ListNode | null {
    let start = list1;
    for (let i = 1; i < a; i++) {
        start = start.next;
    }
    let end = start.next;
    for (let i = 0; i < b - a + 1; i++) {
        end = end.next;
    }
    let tail = list2;
    while(tail.next !== null) {
        tail = tail.next;
    }
    start.next = list2;
    tail.next = end;
    return list1;
};

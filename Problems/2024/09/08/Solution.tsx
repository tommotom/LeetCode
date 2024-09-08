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

function splitListToParts(head: ListNode | null, k: number): Array<ListNode | null> {
    let length = 0, node = head;
    while (node !== null) {
        length++;
        node = node.next;
    }
    node = head;
    const ans = [...Array(k)].map(_ => null);
    for (let i = 0; i < k; i++) {
        if (node === null) {
            break;
        }
        ans[i] = node;
        const target = Math.ceil(length / (k - i));
        for (let j = 0; j < target-1; j++) {
            node = node.next;
        }
        const tmp = node.next;
        node.next = null;
        node = tmp;
        length -= target;
    }
    return ans;
};

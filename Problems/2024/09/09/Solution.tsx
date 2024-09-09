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

function spiralMatrix(m: number, n: number, head: ListNode | null): number[][] {
    const arr = Array(m).fill(0).map(_ => Array(n).fill(-1));
    const dir = [[0,1], [1,0], [0,-1], [-1,0]];
    let d = 0, r = 0, c = 0;
    while (head !== null) {
        arr[r][c] = head.val;
        head = head.next;
        if (head === null) {
            break;
        }
        while (!arr[r + dir[d][0]] || arr[r + dir[d][0]][c + dir[d][1]] !== -1) {
            d = (d + 1) % 4;
        }
        r += dir[d][0];
        c += dir[d][1];
    }
    return arr;
};

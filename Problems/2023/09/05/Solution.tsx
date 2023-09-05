/**
 * Definition for Node.
 * class Node {
 *     val: number
 *     next: Node | null
 *     random: Node | null
 *     constructor(val?: number, next?: Node, random?: Node) {
 *         this.val = (val===undefined ? 0 : val)
 *         this.next = (next===undefined ? null : next)
 *         this.random = (random===undefined ? null : random)
 *     }
 * }
 */

function copyRandomList(head: Node | null): Node | null {
    const dummy = new Node();
    const nodes = []
    let i = 0;
    let node = head;
    let cur = dummy;
    while (node !== null) {
        cur.next = new Node(node.val);
        cur = cur.next;
        nodes.push(cur);
        node.val = i++;
        node = node.next;
    }
    i = 0;
    node = head;
    cur = dummy.next;
    while (node !== null) {
        if (node.random !== null) {
            cur.random = nodes[node.random.val];
        }
        cur = cur.next;
        node = node.next;
    }
    return dummy.next;
};

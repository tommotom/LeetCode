class Node {

    next: Node;
    prev: Node;
    count: number;
    keys: Set<string>;

    constructor() {
        this.count = 0;
        this.keys = new Set();
    }
}

class AllOne {

    head: Node;
    tail: Node;
    map: Map<string, Node>;

    constructor() {
        this.head = new Node();
        this.tail = new Node();
        this.head.next = this.tail;
        this.tail.prev = this.head;
        this.map = new Map();
    }

    inc(key: string): void {
        const cur = this.map.has(key) ? this.map.get(key) : this.tail;
        cur.keys.delete(key);
        if (cur.prev.count !== cur.count + 1) {
            const newNode = new Node();
            newNode.count = cur.count + 1;
            cur.prev.next = newNode;
            newNode.prev = cur.prev;
            newNode.next = cur;
            cur.prev = newNode;
        }
        cur.prev.keys.add(key);
        this.map.set(key, cur.prev);
        this.deleteIfEmpty(cur);
    }

    dec(key: string): void {
        const cur = this.map.get(key);
        cur.keys.delete(key);
        if (cur.count === 1) {
            this.map.delete(key);
            this.deleteIfEmpty(cur);
            return;
        }
        if (cur.next.count !== cur.count-1) {
            const newNode = new Node();
            newNode.count = cur.count-1;
            cur.next.prev = newNode;
            newNode.next = cur.next;
            newNode.prev = cur;
            cur.next = newNode;
        }
        cur.next.keys.add(key);
        this.map.set(key, cur.next);
        this.deleteIfEmpty(cur);
    }

    deleteIfEmpty(node: Node): void {
        if (node.keys.size > 0 || node === this.tail) {
            return;
        }
        node.prev.next = node.next;
        node.next.prev = node.prev;
    }

    getMaxKey(): string {
        for (const key of this.head.next.keys) {
            return key;
        }
        return "";
    }

    getMinKey(): string {
        for (const key of this.tail.prev.keys) {
            return key;
        }
        return "";
    }
}

/**
 * Your AllOne object will be instantiated and called as such:
 * var obj = new AllOne()
 * obj.inc(key)
 * obj.dec(key)
 * var param_3 = obj.getMaxKey()
 * var param_4 = obj.getMinKey()
 */

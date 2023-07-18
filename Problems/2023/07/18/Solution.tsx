class MyNode {
    prev: MyNode;
    next: MyNode;
    key: number;
    value: number;
}

class LRUCache {

    head: MyNode;
    tail: MyNode;
    cap: number;
    map: Map<number, MyNode> = new Map();

    constructor(capacity: number) {
        this.cap = capacity;
        this.head = new MyNode();
        this.tail = new MyNode();
        this.head.next = this.tail;
        this.tail.prev = this.head;
    }

    get(key: number): number {
        if (this.map.has(key)) {
            this.toTop(key);
            return this.map.get(key).value;
        }
        return -1;
    }

    put(key: number, value: number): void {
        if (this.map.has(key)) {
            this.toTop(key);
            this.map.get(key).value = value;
            return;
        }
        const node: MyNode = new MyNode();
        node.key = key;
        node.value = value;
        this.map.set(key, node);
        this.toTop(key);
        this.cap--;

        if (this.cap == -1) {
            const toBeDeleted: MyNode = this.tail.prev;
            this.map.delete(toBeDeleted.key);
            toBeDeleted.prev.next = this.tail;
            this.tail.prev = toBeDeleted.prev;
            toBeDeleted.next = null;
            toBeDeleted.prev = null;
            this.cap++;
        }
    }

    toTop(key: number): void {
        const node: MyNode = this.map.get(key);
        const old: MyNode = this.head.next;
        if (node === old) {
            return;
        }
        if (node.prev !== undefined) {
            node.prev.next = node.next;
            node.next.prev = node.prev;
        }
        old.prev = node;
        node.next = old;
        node.prev = this.head;
        this.head.next = node;
    }
}

/**
 * Your LRUCache object will be instantiated and called as such:
 * var obj = new LRUCache(capacity)
 * var param_1 = obj.get(key)
 * obj.put(key,value)
 */

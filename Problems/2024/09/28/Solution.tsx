class Node {
    prev: Node;
    next: Node;
    val: number;

    constructor(val: number) {
        this.val = val;
    }
}

class MyCircularDeque {

    left: number;
    head: Node;
    tail: Node;

    constructor(k: number) {
        this.left = k;
        this.head = new Node(-1);
        this.tail = new Node(-1);
        this.head.next = this.tail
        this.tail.prev = this.head;
    }

    insertFront(value: number): boolean {
        if (this.isFull()) {
            return false;
        }
        const node = new Node(value);
        this.head.next.prev = node;
        node.next = this.head.next;
        node.prev = this.head;
        this.head.next = node;
        this.left--;
        return true;
    }

    insertLast(value: number): boolean {
        if (this.isFull()) {
            return false;
        }
        const node = new Node(value);
        this.tail.prev.next = node;
        node.prev = this.tail.prev;
        node.next = this.tail;
        this.tail.prev = node;
        this.left--;
        return true;
    }

    deleteFront(): boolean {
        if (this.isEmpty()) {
            return false;
        }
        this.head.next.next.prev = this.head;
        this.head.next = this.head.next.next;
        this.left++;
        return true;
    }

    deleteLast(): boolean {
        if (this.isEmpty()) {
            return false;
        }
        this.tail.prev.prev.next = this.tail
        this.tail.prev = this.tail.prev.prev;
        this.left++;
        return true;
    }

    getFront(): number {
        return this.head.next.val;
    }

    getRear(): number {
        return this.tail.prev.val;
    }

    isEmpty(): boolean {
        return this.head.next === this.tail;
    }

    isFull(): boolean {
        return this.left === 0;
    }
}

/**
 * Your MyCircularDeque object will be instantiated and called as such:
 * var obj = new MyCircularDeque(k)
 * var param_1 = obj.insertFront(value)
 * var param_2 = obj.insertLast(value)
 * var param_3 = obj.deleteFront()
 * var param_4 = obj.deleteLast()
 * var param_5 = obj.getFront()
 * var param_6 = obj.getRear()
 * var param_7 = obj.isEmpty()
 * var param_8 = obj.isFull()
 */
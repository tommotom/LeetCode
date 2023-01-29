class Node {

    int key;
    int val;
    int freq;
    Node prev;
    Node next;

    Node(int key, int val) {
        this.key = key;
        this.val = val;
        this.freq = 1;
    }
}

class DoublyLinkedList {

    int size;
    Node head;
    Node tail;

    DoublyLinkedList() {
        this.size = 0;
        this.head = new Node(0, 0);
        this.tail = new Node(0, 0);
        head.next = tail;
        tail.prev = head;
    }

    void add(Node node) {
        Node cur = head.next;
        head.next = node;
        node.prev = head;
        node.next = cur;
        cur.prev = node;
        size++;
    }

    void remove(Node node) {
        Node prev = node.prev;
        Node next = node.next;
        prev.next = next;
        next.prev = prev;
        size--;
    }
}

class LFUCache {

    int cap;
    int size;
    int min;
    Map<Integer, Node> keyToNode;
    Map<Integer, DoublyLinkedList> freqs;

    public LFUCache(int capacity) {
        this.cap = capacity;
        this.size = 0;
        this.min = 0;
        keyToNode = new HashMap<>();
        freqs = new HashMap<>();
    }

    public int get(int key) {
        if (!keyToNode.containsKey(key)) {
            return -1;
        }
        update(keyToNode.get(key));
        return keyToNode.get(key).val;
    }

    public void put(int key, int value) {
        if (cap == 0) {
            return;
        }

        if (keyToNode.containsKey(key)) {
            Node cur = keyToNode.get(key);
            cur.val = value;
            update(cur);
        } else {
            size++;
            if (size > cap) {
                DoublyLinkedList dll = freqs.get(min);
                keyToNode.remove(dll.tail.prev.key);
                dll.remove(dll.tail.prev);
                size--;
            }
            min = 1;
            Node node = new Node(key, value);

            DoublyLinkedList dll = freqs.getOrDefault(1, new DoublyLinkedList());
            dll.add(node);
            freqs.put(1, dll);
            keyToNode.put(key, node);
        }
    }

    void update(Node node) {
        int freq = node.freq;
        DoublyLinkedList curList = freqs.get(freq);
        curList.remove(node);

        if (freq == min && curList.size == 0) {
            min++;
        }

        node.freq++;
        DoublyLinkedList newList = freqs.getOrDefault(node.freq, new DoublyLinkedList());
        newList.add(node);
        freqs.put(node.freq, newList);
    }
}

/**
 * Your LFUCache object will be instantiated and called as such:
 * LFUCache obj = new LFUCache(capacity);
 * int param_1 = obj.get(key);
 * obj.put(key,value);
 */

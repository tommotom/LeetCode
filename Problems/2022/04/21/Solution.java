class Node {

  public int val;
  public Node next;

  public Node(int val) {
    this.val = val;
  }
}

class MyLinkedList {

  private Node head;
  private Node tail;

  public MyLinkedList() {
    this.head = new Node(0);
    this.tail = this.head;
  }

  public boolean contains(int val) {
    Node node = this.head.next;
    while (node != null) {
      if (node.val == val) {
        return true;
      }
      node = node.next;
    }
    return false;
  }

  public void add(Node node) {
    if (contains(node.val)) {
      return;
    }
    this.tail.next = node;
    this.tail = this.tail.next;
  }

  public void remove(int val) {
    Node node = this.head;
    while (node != null && node.next != null && node.next.val != val) {
      node = node.next;
    }
    if (node == null || node.next == null) {
      return;
    }
    if (this.tail == node.next) {
      this.tail = node;
    }
    node.next = node.next.next;
  }
}

class MyHashSet {

  private MyLinkedList[] arr;

  public MyHashSet() {
    arr = new MyLinkedList[10000];
  }

  public void add(int key) {
    int hashed = hash(key);
    if (arr[hashed] == null) {
      arr[hashed] = new MyLinkedList();
    }
    arr[hashed].add(new Node(key));
  }

  public void remove(int key) {
    int hashed = hash(key);
    if (arr[hashed] == null) {
      return;
    }
    arr[hashed].remove(key);
  }

  public boolean contains(int key) {
    int hashed = hash(key);
    return arr[hashed] != null && arr[hashed].contains(key);
  }

  public int hash(int key){
    return key % 10000;
  }
}

/**
 * Your MyHashSet object will be instantiated and called as such:
 * MyHashSet obj = new MyHashSet();
 * obj.add(key);
 * obj.remove(key);
 * boolean param_3 = obj.contains(key);
 */

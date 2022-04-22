class Node {

  public int key;
  public int val;
  public Node next;

  public Node(int key, int val) {
    this.key = key;
    this.val = val;
  }
}

class MyLinkedList {

  private Node head;
  private Node tail;

  public MyLinkedList() {
    this.head = new Node(0, 0);
    this.tail = this.head;
  }

  public int get(int key) {
    Node node = this.head.next;
    while (node != null) {
      if (node.key == key) {
        return node.val;
      }
      node = node.next;
    }
    return -1;
  }

  public void put(Node add) {
    Node node = this.head;
    while (node.next != null) {
      if (node.next.key == add.key) {
        node.next.val = add.val;
        return;
      }
      node = node.next;
    }
    node.next = add;
  }

  public void remove(int key) {
    Node node = this.head;
    while (node.next != null && node.next.key != key) {
      node = node.next;
    }
    if (node.next == null) {
      return;
    }
    node.next = node.next.next;
  }
}

class MyHashMap {

  private MyLinkedList[] arr;

  public MyHashMap() {
    arr = new MyLinkedList[100000];
  }

  public void put(int key, int value) {
    int hashed = hash(key);
    if (arr[hashed] == null) {
      arr[hashed] = new MyLinkedList();
    }
    arr[hashed].put(new Node(key, value));

  }

  public int get(int key) {
    int hashed = hash(key);
    if (arr[hashed] == null) {
      return -1;
    }
    return arr[hashed].get(key);
  }

  public void remove(int key) {
    int hashed = hash(key);
    if (arr[hashed] == null) {
      return;
    }
    arr[hashed].remove(key);
  }

  public int hash(int key) {
    return key % 100000;
  }
}

/**
 * Your MyHashMap object will be instantiated and called as such:
 * MyHashMap obj = new MyHashMap();
 * obj.put(key,value);
 * int param_2 = obj.get(key);
 * obj.remove(key);
 */

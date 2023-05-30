class MyHashSet {

    boolean[][] arr = new boolean[1001][1001];

    public MyHashSet() {

    }

    public void add(int key) {
        arr[key/1000][key%1000] = true;
    }

    public void remove(int key) {
        arr[key/1000][key%1000] = false;
    }

    public boolean contains(int key) {
        return arr[key/1000][key%1000];
    }
}

/**
 * Your MyHashSet object will be instantiated and called as such:
 * MyHashSet obj = new MyHashSet();
 * obj.add(key);
 * obj.remove(key);
 * boolean param_3 = obj.contains(key);
 */

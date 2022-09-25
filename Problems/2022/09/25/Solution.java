class MyCircularQueue {

    private int[] q;
    private int size;
    private int k;
    private int f;
    private int r;

    public MyCircularQueue(int k) {
        q = new int[k];
        Arrays.fill(q, -1);
        this.k = k;
        this.f = 0;
        this.r = -1;
    }

    public boolean enQueue(int value) {
        if (this.isFull()) {
            return false;
        }
        size++;
        r = (r+1) % k;
        q[r] = value;
        return true;
    }

    public boolean deQueue() {
        if (this.isEmpty()) {
            return false;
        }
        size--;
        q[f] = -1;
        f = (f+1) % k;
        return true;
    }

    public int Front() {
        if (this.isEmpty()) {
            return -1;
        }
        return q[f];
    }

    public int Rear() {
        if (this.isEmpty()) {
            return -1;
        }
        return q[r];
    }

    public boolean isEmpty() {
        return size == 0;
    }

    public boolean isFull() {
        return k == size;
    }
}

/**
 * Your MyCircularQueue object will be instantiated and called as such:
 * MyCircularQueue obj = new MyCircularQueue(k);
 * boolean param_1 = obj.enQueue(value);
 * boolean param_2 = obj.deQueue();
 * int param_3 = obj.Front();
 * int param_4 = obj.Rear();
 * boolean param_5 = obj.isEmpty();
 * boolean param_6 = obj.isFull();
 */

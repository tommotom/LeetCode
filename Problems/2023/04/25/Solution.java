class SmallestInfiniteSet {

    private final PriorityQueue<Integer> q;
    private int i;

    public SmallestInfiniteSet() {
        q = new PriorityQueue<>();
        i = 1;
    }

    public int popSmallest() {
        if (q.isEmpty()) {
            return i++;
        }
        int num = q.poll();
        while (!q.isEmpty() && q.peek() == num) {
            q.poll();
        }
        return num;
    }

    public void addBack(int num) {
        if (i <= num) {
            return;
        }
        q.add(num);
    }
}

/**
 * Your SmallestInfiniteSet object will be instantiated and called as such:
 * SmallestInfiniteSet obj = new SmallestInfiniteSet();
 * int param_1 = obj.popSmallest();
 * obj.addBack(num);
 */

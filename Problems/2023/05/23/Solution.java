class KthLargest {

    private final int k;
    private final PriorityQueue<Integer> q;

    public KthLargest(int k, int[] nums) {
        this.k = k;
        this.q = new PriorityQueue<>((a, b) -> a - b);
        for (int num : nums) {
            add(num);
        }
    }

    public int add(int val) {
        q.add(val);
        if (q.size() > k) {
            q.poll();
        }
        return q.peek();
    }
}

/**
 * Your KthLargest object will be instantiated and called as such:
 * KthLargest obj = new KthLargest(k, nums);
 * int param_1 = obj.add(val);
 */

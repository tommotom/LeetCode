class KthLargest {

  private PriorityQueue<Integer> q;
  private int k;

  public KthLargest(int k, int[] nums) {
    q = new PriorityQueue<>();
    for (int num: nums) {
      q.add(num);
    }
    while (q.size() > k) {
      q.poll();
    }
    this.k = k;
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

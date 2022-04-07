class Solution {
  public int lastStoneWeight(int[] stones) {
    PriorityQueue<Integer> q = new PriorityQueue<>(Collections.reverseOrder());
    for (int s: stones) {
      q.add(s);
    }

    while (q.size() > 1) {
      int x = q.poll();
      int y = q.poll();
      if (x == y) {
        continue;
      }
      q.add(x-y);
    }

    return q.size() > 0 ? q.poll() : 0;
  }
}

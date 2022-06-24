class Solution {
  public boolean isPossible(int[] target) {
    if (target.length == 1) {
      return target[0] == 1;
    }

    PriorityQueue<Integer> q = new PriorityQueue<>((a, b) -> b-a);
    int sum = 0;
    for (int t : target) {
      sum += t;
      q.add(t);
    }

    while (q.peek() != 1) {
      int cur = q.poll();
      if (sum - cur == 1) {
        return true;
      }

      int x = cur % (sum - cur);
      sum = sum - cur + x;

      if (x == 0 || x == cur) {
        return false;
      }
      q.add(x);
    }
    return true;
  }
}

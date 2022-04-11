class ValCount implements Comparable<ValCount>{

  public Integer val;
  public Integer count;

  public ValCount(Integer val, Integer count) {
    this.val = val;
    this.count = count;
  }

  @Override
  public int compareTo(ValCount other) {
    return Integer.compare(this.count, other.count);
  }
}

class Solution {
  public int[] topKFrequent(int[] nums, int k) {
    Map<Integer, Integer> map = new HashMap<>();
    for (int num: nums) {
      map.put(num, map.getOrDefault(num, 0) + 1);
    }

    PriorityQueue<ValCount> q = new PriorityQueue<>(Collections.reverseOrder());
    for (Integer key: map.keySet()) {
      q.add(new ValCount(key, map.get(key)));
    }

    int[] ans = new int[k];
    for (int i = 0; i < k; i++) {
      ans[i] = q.poll().val;
    }

    return ans;
  }
}

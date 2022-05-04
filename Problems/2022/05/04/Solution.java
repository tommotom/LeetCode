class Solution {
  public int maxOperations(int[] nums, int k) {
    HashMap<Integer, Integer> counter = new HashMap<>();
    int ans = 0;
    for (int num : nums) {
      int pairCount = counter.getOrDefault(k-num, 0);
      if (pairCount > 0) {
        counter.put(k-num, counter.get(k-num) - 1);
        ans++;
      } else {
        counter.put(num, counter.getOrDefault(num, 0) + 1);
      }
    }
    return ans;
  }
}

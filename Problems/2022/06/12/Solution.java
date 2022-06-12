class Solution {
  public int maximumUniqueSubarray(int[] nums) {
    int[] cum = new int[nums.length];
    cum[0] = nums[0];
    for (int i = 1; i < nums.length; i++) {
      cum[i] = cum[i-1] + nums[i];
    }

    int[] last = new int[10001];
    Arrays.fill(last, -1);
    int ans = 0, sum = 0, validFrom = 0;
    for (int i = 0; i < nums.length; i++) {
      if (last[nums[i]] >= 0) {
        validFrom = Math.max(validFrom, last[nums[i]]);
        sum = cum[i-1] - cum[validFrom];
      }
      sum += nums[i];
      last[nums[i]] = i;
      ans = Math.max(ans, sum);
    }
    return ans;
  }
}

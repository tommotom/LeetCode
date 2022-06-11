class Solution {
  public int minOperations(int[] nums, int x) {
    int n = nums.length;
    int sum = Arrays.stream(nums).sum();

    if (sum == x) {
      return n;
    }

    if (sum < x) {
      return -1;
    }

    int exclude = 0, l = -1, r = 0, ans = n+1;
    while (l+1 < n) {
      if (r < n && sum - exclude >= x) {
        exclude += nums[r];
        r++;
      } else {
        l++;
        exclude -= nums[l];
      }
      if (sum - exclude == x) {
        ans = Math.min(ans, n - (r - l - 1));
      }
    }

    return ans == n + 1 ? -1 : ans;
  }
}

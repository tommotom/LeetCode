class Solution {
  public int splitArray(int[] nums, int m) {
    int sum = Arrays.stream(nums).sum();
    int l = 0, r = sum;
    while (l < r) {
      int ans = l + (r - l) / 2;
      if (!isValid(nums, m, ans)) {
        l = ans + 1;
      } else {
        r = ans;
      }
    }
    return l;
  }

  private boolean isValid(int[] nums, int m, int ans) {
    int sum = 0, split = 1;
    for (int num: nums) {
      if (num > ans) {
        return false;
      }

      if (sum + num > ans) {
        split++;
        sum = 0;
      }
      sum += num;
    }
    return split <= m;
  }
}

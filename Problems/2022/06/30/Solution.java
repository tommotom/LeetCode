class Solution {
  public int minMoves2(int[] nums) {
    Arrays.sort(nums);
    int ans = 0;
    int l = 0, r = nums.length-1;
    while (l < r) {
      ans += (l+1) * (nums[l+1] - nums[l]);
      l++;

      if (l == r) {
        break;
      }

      ans += (nums.length-r) * (nums[r] - nums[r-1]);
      r--;
    }
    return ans;
  }
}

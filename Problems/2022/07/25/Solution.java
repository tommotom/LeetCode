class Solution {
  public int[] searchRange(int[] nums, int target) {
    int l = 0, r = nums.length;
    while (l < r) {
      int m = l + (r - l) / 2;
      if (nums[m] < target) {
        l = m + 1;
      } else {
        r = m;
      }
    }
    if (l == nums.length || nums[l] != target) {
      return new int[] {-1, -1};
    }

    int start = l;

    l = 0;
    r = nums.length;
    while (l < r) {
      int m = l + (r - l) / 2;
      if (nums[m] <= target) {
        l = m + 1;
      } else {
        r = m;
      }
    }
    int end = l;
    if (end == nums.length || nums[end] != target) {
      end--;
    }
    return new int[] {start, end};
  }
}

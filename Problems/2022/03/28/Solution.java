class Solution {
  public boolean search(int[] nums, int target) {
    int l = 0, r = nums.length, last = nums[nums.length-1];
    while (l < r) {
      int m = l + (r - l) / 2;
      if (nums[m] == target) {
        return true;
      }

      while (l < m && nums[l] == nums[m]) {
        l++;
      }
      if (nums[l] == target) {
        return true;
      }

      while (m < r-1 && nums[r-1] == nums[m]) {
        r--;
      }
      if (nums[r-1] == target) {
        return true;
      }

      if (nums[m] < nums[r-1] && nums[m] < target && target < nums[r-1]) {
        l = m + 1;
      } else if (nums[m] > nums[r-1] && (nums[m] < target || target < nums[r-1])) {
        l = m + 1;
      } else {
        r = m;
      }

    }
    return false;
  }
}
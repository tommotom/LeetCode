class Solution {
  public boolean checkPossibility(int[] nums) {
    boolean skipped = false;
    for (int i = 1; i < nums.length; i++) {
      if (nums[i-1] <= nums[i]) {
        continue;
      }
      if (skipped) {
        return false;
      }
      if (i > 1 && nums[i-2] > nums[i]) {
        nums[i] = nums[i-1];
      } else {
        nums[i-1] = nums[i];
      }
      skipped = true;
    }
    return true;
  }
}

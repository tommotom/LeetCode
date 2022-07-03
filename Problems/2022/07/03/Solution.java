class Solution {
  public int wiggleMaxLength(int[] nums) {
    int n = nums.length;

    int a = 1;
    boolean up = true;
    for (int i = 1; i < n; i++) {
      if (up && nums[i-1] > nums[i]) {
        a++;
        up = false;
      } else if (!up && nums[i-1] < nums[i]) {
        a++;
        up = true;
      }
    }

    int b = 1;
    up = false;
    for (int i = 1; i < n; i++) {
      if (up && nums[i-1] > nums[i]) {
        b++;
        up = false;
      } else if (!up && nums[i-1] < nums[i]) {
        b++;
        up = true;
      }
    }

    return Math.max(a, b);
  }
}

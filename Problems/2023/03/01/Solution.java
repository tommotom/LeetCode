class Solution {
    public int[] sortArray(int[] nums) {
        helper(nums, 0, nums.length);
        return nums;
    }

    private void helper(int[] nums, int l, int r) {
        if (l+1 == r) {
            return;
        }
        int m = l + (r - l) / 2;
        helper(nums, l, m);
        helper(nums, m, r);

        int[] merged = new int[r-l];
        int left = l, right = m;
        for (int i = 0; i < merged.length; i++) {
            int val;
            if (left == m) {
                val = nums[right];
                right++;
            } else if (right == r) {
                val = nums[left];
                left++;
            } else if (nums[left] < nums[right]) {
                val = nums[left];
                left++;
            } else {
                val = nums[right];
                right++;
            }

            merged[i] = val;
        }

        for (int i = 0; i < merged.length; i++) {
            nums[l + i] = merged[i];
        }
    }
}

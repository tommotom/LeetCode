class Solution {
    public int singleNonDuplicate(int[] nums) {
        int l = 0, r = nums.length-1;
        while (l < r) {
            int m = l + (r - l) / 2;
            if (m % 2 == 0) {
                if (nums[m] != nums[m+1]) {
                    r = m;
                } else {
                    l = m + 1;
                }
            } else {
                if (nums[m] != nums[m-1]) {
                    r = m;
                } else {
                    l = m + 1;
                }
            }
        }
        return l == nums.length-2 && l % 2 == 1 ? nums[l+1] : nums[l];
    }
}

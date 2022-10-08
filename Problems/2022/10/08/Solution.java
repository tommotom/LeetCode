class Solution {
    public int threeSumClosest(int[] nums, int target) {
        Arrays.sort(nums);
        int ans = nums[0] + nums[1] + nums[2];
        for (int i = 1; i < nums.length-1; i++) {
            int l = 0, r = nums.length-1;
            while (l < r) {
                int sum = nums[i] + nums[l] + nums[r];
                if (l != i && r != i) {
                    if (Math.abs(ans - target) > Math.abs(sum - target)) {
                        ans = sum;
                    }
                }
                if (sum < target) {
                    l++;
                } else {
                    r--;
                }
            }
        }
        return ans;
    }
}

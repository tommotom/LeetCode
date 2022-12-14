class Solution {
    public int rob(int[] nums) {
        int prev1 = 0, prev2 = 0;
        for (int i = 0; i < nums.length; i++) {
            int tmp = Math.max(prev1, prev2 + nums[i]);
            prev2 = prev1;
            prev1 = tmp;
        }
        return prev1;
    }
}

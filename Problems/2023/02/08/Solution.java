class Solution {
    public int jump(int[] nums) {
        int n = nums.length;
        int ans = 0;
        int curEnd = 0;
        int curFarest = 0;
        for (int i = 0; i < n-1; i++) {
            curFarest = Math.max(curFarest, i + nums[i]);
            if (i == curEnd) {
                ans++;
                curEnd = curFarest;
            }
        }
        return ans;
    }
}

class Solution {
    public long countSubarrays(int[] nums, int minK, int maxK) {
        int from = 0, minI = -1, maxI = -1;
        long ans = 0;
        for (int i = 0 ; i < nums.length; i++) {
            int num = nums[i];
            if (num < minK || maxK < num) {
                minI = -1;
                maxI = -1;
                from = i + 1;
            }
            if (num == minK) {
                minI = i;
            }
            if (num == maxK) {
                maxI = i;
            }
            ans += Math.max(0, Math.min(minI, maxI) - from + 1);
        }
        return ans;
    }
}

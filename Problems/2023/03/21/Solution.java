class Solution {
    public long zeroFilledSubarray(int[] nums) {
        long ans = 0;
        long zeros = 0;
        for (int num : nums) {
            if (num == 0) {
                zeros++;
            } else {
                zeros = 0;
            }
            ans += zeros;
        }
        return ans;
    }
}

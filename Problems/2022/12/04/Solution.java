class Solution {
    public int minimumAverageDifference(int[] nums) {
        int n = nums.length, index = 0;
        long min = Integer.MAX_VALUE, rest = 0, sum = 0;
        for (int i = 0; i < n; i++) {
            rest += nums[i];
        }
        for (int i = 0; i < n; i++) {
            sum += nums[i];
            rest -= nums[i];
            long left = sum / (i+1);
            long right = rest / (i == n-1 ? 1 : (n-i-1));
            long tmp = Math.abs(left - right);
            if (tmp < min) {
                min = tmp;
                index = i;
            }
        }
        return index;
    }
}

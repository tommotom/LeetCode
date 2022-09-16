class Solution {

    private Integer[][] memo;
    private int[] nums;
    private int[] multipliers;
    private int n;
    private int m;

    public int maximumScore(int[] nums, int[] multipliers) {
        this.n = nums.length;
        this.m = multipliers.length;
        this.nums = nums;
        this.multipliers = multipliers;
        this.memo = new Integer[m][m];
        return helper(0, 0);
    }

    private int helper(int l, int j) {
        if (j == m) {
            return 0;
        }

        if (memo[l][j] != null) {
            return memo[l][j];
        }

        int left = nums[l] * multipliers[j] + helper(l+1, j+1);
        int right = nums[(n-1) - (j - l)] * multipliers[j] + helper(l, j+1);
        memo[l][j] = Math.max(left, right);
        return memo[l][j];
    }
}

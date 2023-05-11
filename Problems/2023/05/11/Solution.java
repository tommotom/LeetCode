class Solution {
    public int maxUncrossedLines(int[] nums1, int[] nums2) {
        int n = nums1.length, m = nums2.length, ans = 0;
        int[][] dp = new int[n][m];
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (nums1[i] == nums2[j]) {
                    int prev = i == 0 || j == 0 ? 0 : dp[i-1][j-1];
                    dp[i][j] = Math.max(dp[i][j], prev + 1);
                }
                if (i > 0) {
                    dp[i][j] = Math.max(dp[i][j], dp[i-1][j]);
                }
                if (j > 0) {
                    dp[i][j] = Math.max(dp[i][j], dp[i][j-1]);
                }
                ans = Math.max(ans, dp[i][j]);
            }
        }
        return ans;
    }
}

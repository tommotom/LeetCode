class Solution {
    public int longestCommonSubsequence(String text1, String text2) {
        int m = text1.length(), n = text2.length();
        int[][]dp = new int[m][n];
        int ans = 0;
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (text1.charAt(i) == text2.charAt(j)) {
                    dp[i][j] = i > 0 && j > 0 ? dp[i-1][j-1] + 1 : 1;
                } else {
                    if (j > 0) {
                        dp[i][j] = Math.max(dp[i][j], dp[i][j-1]);
                    }
                    if (i > 0) {
                        dp[i][j] = Math.max(dp[i][j], dp[i-1][j]);
                    }
                }
                ans = Math.max(ans, dp[i][j]);
            }
        }
        return ans;
    }
}

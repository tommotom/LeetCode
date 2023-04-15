class Solution {
    public int longestPalindromeSubseq(String s) {
        int n = s.length();
        int[][] dp = new int[n][n];
        for (int r = 0; r < n; r++) {
            dp[r][r] = 1;
        }
        for (int r = n-1; r >= 0; r--) {
            for (int c = r+1; c < n; c++) {
                if (s.charAt(r) == s.charAt(c)) {
                    dp[r][c] = dp[r+1][c-1] + 2;
                } else {
                    dp[r][c] = Math.max(dp[r+1][c], dp[r][c-1]);
                }
            }
        }
        return dp[0][n-1];
    }
}

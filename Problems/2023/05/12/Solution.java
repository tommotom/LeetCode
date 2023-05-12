class Solution {
    public long mostPoints(int[][] questions) {
        int n = questions.length;
        long[] dp = new long[n+1];
        for (int i = 0; i < n; i++) {
            dp[i+1] = Math.max(dp[i+1], dp[i]);
            int p = questions[i][0], b = questions[i][1];
            int j = Math.min(i+b+1, n);
            dp[j] = Math.max(dp[j], dp[i]+p);
        }
        return dp[n];
    }
}

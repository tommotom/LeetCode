class Solution {
    public int numTilings(int n) {
        if (n == 1) {return 1;}

        int mod = 1000000007;

        long[][] dp = new long[2][n+1];
        dp[0][1] = 1;
        dp[0][2] = 2;
        dp[1][2] = 2;

        for (int i = 3; i <= n; i++) {
            dp[0][i] = (dp[0][i-1] + dp[0][i-2] + dp[1][i-1]) % mod;
            dp[1][i] = (dp[1][i-1] + dp[0][i-2] * 2) % mod;
        }
        return (int) dp[0][n];
    }
}

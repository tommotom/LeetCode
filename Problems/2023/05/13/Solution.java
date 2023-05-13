class Solution {

    private static final int mod = 1000000007;

    public int countGoodStrings(int low, int high, int zero, int one) {
        int mod = 1000000007;
        long[] dp = new long[high+1];
        dp[0] = 1;
        long ans = 0;
        for (int i = 0; i < high+1; i++) {
            if (i + zero < high+1) {
                dp[i+zero] = (dp[i+zero] + dp[i]) % mod;
            }
            if (i + one < high+1) {
                dp[i+one] = (dp[i+one] + dp[i]) % mod;
            }
            if (low <= i) {
                ans = (ans + dp[i]) % mod;
            }
        }
        return (int) ans;
    }
}

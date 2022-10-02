class Solution {

    Integer[][] memo;
    int k;
    int mod = 1000000007;

    public int numRollsToTarget(int n, int k, int target) {
        memo = new Integer[n+1][target+1];
        this.k = k;
        return helper(n, target);
    }

    public int helper(int n, int target) {
        if (n == 0 && target == 0) {
            return 1;
        }
        if (n < 0 || target < 0) {
            return 0;
        }
        if (memo[n][target] != null) {
            return memo[n][target];
        }
        long ret = 0;
        for (int i = 1; i <= k; i++) {
            ret += helper(n-1, target-i);
            ret %= mod;
        }
        memo[n][target] = (int) ret;
        return (int) ret;
    }
}

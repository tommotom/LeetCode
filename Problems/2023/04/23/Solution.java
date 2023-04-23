class Solution {

    private static final int MOD = 1000000007;
    private Map<Long, Integer>[] memo;
    private String s;
    private int k;

    public int numberOfArrays(String s, int k) {
        this.memo = new Map[s.length()];
        this.s = s;
        this.k = k;
        return dp(0, 0);
    }

    private int dp(int i, long sum) {
        if (i == s.length()) {return sum > 0 ? 1 : 0;}
        sum = sum * 10 + Character.getNumericValue(s.charAt(i));
        if (sum > k || sum == 0) {return 0;}
        if (memo[i] == null) {memo[i] = new HashMap<>();}
        if (!memo[i].containsKey(sum)) {
            memo[i].put(sum, (dp(i+1, sum) + dp(i+1, 0)) % MOD);
        }
        return memo[i].get(sum);
    }
}

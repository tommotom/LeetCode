class Solution {

    private String s;
    private int[][] memo;

    public int minInsertions(String s) {
        this.s = s;
        this.memo = new int[s.length()][s.length()];
        return dp(0, s.length()-1);
    }

    private int dp(int l, int r) {
        if (l >= r) {
            return 0;
        }
        if (memo[l][r] == 0) {
            memo[l][r] = s.charAt(l) == s.charAt(r)
                    ? dp(l+1, r-1)
                    : Math.min(dp(l+1, r), dp(l, r-1)) + 1;
        }
        return memo[l][r];
    }
}

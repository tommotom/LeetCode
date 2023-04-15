class Solution {

    private int[][] dp;

    public int maxValueOfCoins(List<List<Integer>> piles, int k) {
        dp = new int[piles.size()][k+1];
        return dp(0, k, piles);
    }

    private int dp(int i, int k, List<List<Integer>> piles) {
        if (i == piles.size() || k == 0) {return 0;}
        if (dp[i][k] > 0) {return dp[i][k];}
        int res = dp(i+1, k, piles), cur = 0;
        for (int j = 0; j < piles.get(i).size() && k-j-1 >= 0; j++) {
            cur += piles.get(i).get(j);
            res = Math.max(res, dp(i+1, k-j-1, piles) + cur);
        }
        dp[i][k] = res;
        return res;
    }
}

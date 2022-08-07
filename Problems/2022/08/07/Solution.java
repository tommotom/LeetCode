class Solution {
    public int countVowelPermutation(int n) {
        HashMap<Integer, List<Integer>> dir = new HashMap<>();
        dir.put(0, Arrays.asList(1));
        dir.put(1, Arrays.asList(0,2));
        dir.put(2, Arrays.asList(0,1,3,4));
        dir.put(3, Arrays.asList(2,4));
        dir.put(4, Arrays.asList(0));

        int mod = 1000000007;

        int[][] dp = new int[5][n+1];
        for (int i = 0; i < 5; i++) {
            dp[i][1] = 1;
        }
        for (int j = 2; j < n+1; j++) {
            for (int i = 0; i < 5; i++) {
                for (int k : dir.get(i)) {
                    dp[i][j] = (dp[i][j] + dp[k][j-1]) % mod;
                }
            }
        }

        int ans = 0;
        for (int i = 0; i < 5; i++) {
            ans = (ans + dp[i][n]) % mod;
        }
        return ans;
    }
}

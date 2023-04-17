class Solution {
    public int numWays(String[] words, String target) {
        int n = words[0].length(), m = target.length(), mod = 1000000007;

        int[][] count = new int[n][26];
        for (String w : words) {
            for (int i = 0; i < n; i++) {
                count[i][w.charAt(i)-'a']++;
            }
        }

        int[] dp = new int[m+1];
        dp[0] = 1;
        for (int i = 0; i < n; i++) {
            for (int j = m-1; j >= 0; j--) {
                dp[j+1] += (int) ((long)dp[j] * count[i][target.charAt(j)-'a']% mod);
                dp[j+1] %= mod;
            }
        }
        return dp[m];
    }
}

class Solution {
    public int minFlipsMonoIncr(String s) {
        int[][] dp = new int[s.length()][2];
        if (s.charAt(0) == '1') {
            dp[0][0] = 1;
        } else {
            dp[0][1] = 1;
        }
        for (int i = 1; i < s.length(); i++) {
            char c = s.charAt(i);
            if (c == '0') {
                dp[i][0] = dp[i-1][0];
                dp[i][1] = Math.min(dp[i-1][0], dp[i-1][1]) + 1;
            } else {
                dp[i][0] = dp[i-1][0] + 1;
                dp[i][1] = Math.min(dp[i-1][0], dp[i-1][1]);
            }
        }

        return Arrays.stream(dp[s.length()-1]).min().getAsInt();
    }
}

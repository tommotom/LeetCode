class Solution {
    public int mincostTickets(int[] days, int[] costs) {
        int n = days.length;
        int[] dp = new int[n+1];

        int seven = 0, thirty = 0;
        for (int i = 1; i < n+1; i++) {
            while (days[i-1] - days[seven] >= 7) {seven++;}
            while (days[i-1] - days[thirty] >= 30) {thirty++;}
            dp[i] = dp[i-1] + costs[0];
            dp[i] = Math.min(dp[i], dp[seven] + costs[1]);
            dp[i] = Math.min(dp[i], dp[thirty] + costs[2]);
        }
        return dp[n];
    }
}

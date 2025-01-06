impl Solution {
    pub fn mincost_tickets(days: Vec<i32>, costs: Vec<i32>) -> i32 {
        let mut dp = [0; 366];
        let mut i = 0;
        for j in 1..366 {
            if i == days.len() || days[i] > j as i32 {
                dp[j] = dp[j - 1];
            } else {
                dp[j] = dp[j-1] + costs[0];
                dp[j] = dp[j].min(dp[j.max(7)-7] + costs[1]);
                dp[j] = dp[j].min(dp[j.max(30)-30] + costs[2]);
                i += 1;
            }
        }
        dp[365]
    }
}
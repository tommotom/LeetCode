impl Solution {
    pub fn climb_stairs(n: i32, costs: Vec<i32>) -> i32 {
        let n = n as usize;
        let mut dp = vec![i32::MAX; n+1];
        dp[0] = 0;
        for i in 0..n {
            for j in (i+1)..(i+4).min(n+1) {
                let d = (j - i) as i32;
                dp[j] = dp[j].min(dp[i] + costs[j-1] + d * d);
            }
        }
        dp[n]
    }
}

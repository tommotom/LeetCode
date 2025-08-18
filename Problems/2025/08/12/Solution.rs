impl Solution {
    pub fn number_of_ways(n: i32, x: i32) -> i32 {
        const MOD: i64 = 1_000_000_007;
        let n = n as usize;
        let x = x as u32;
        let mut dp = vec![vec![0; n + 1]; n + 1];
        dp[0][0] = 1;
        for i in 1..=n {
            let val = (i as i64).pow(x);
            for j in 0..=n {
                dp[i][j] = dp[i - 1][j];
                if j >= val as usize {
                    dp[i][j] = (dp[i][j] + dp[i - 1][j - val as usize]) % MOD;
                }
            }
        }
        dp[n][n] as i32
    }
}

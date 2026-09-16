impl Solution {
    pub fn number_of_sets(n: i32, k: i32) -> i32 {
        let m = 1000000007_i64;
        let (n, k) = (n as usize, k as usize);
        let mut dp = vec![vec![0_i64; n]; k+1];
        dp[0][0] = 1_i64;
        for i in 0..(k+1) {
            let mut up = 0;
            for j in 1..n {
                dp[i][j] = dp[i][j-1];
                if i > 0 {
                    up += dp[i-1][j-1];
                    up %= m;
                    dp[i][j] += up;
                }
                dp[i][j] %= m;
            }
        }
        dp[k][n-1] as i32
    }
}

impl Solution {
    pub fn new21_game(n: i32, k: i32, max_pts: i32) -> f64 {
        let n = n as usize;
        let k = k as usize;
        let max_pts = max_pts as usize;
        let mut dp = vec![0 as f64; n+1];
        dp[0] = 1.0;
        for i in 0..k {
            for p in 1..(max_pts+1) {
                if i + p > n {
                    break;
                }
                dp[i+p] += dp[i] / (max_pts as f64);
            }
            if i < k {
                dp[i] = 0.0;
            }
        }
        dp.into_iter().sum::<f64>()
    }
}

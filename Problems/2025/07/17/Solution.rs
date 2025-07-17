impl Solution {
    pub fn maximum_length(mut nums: Vec<i32>, k: i32) -> i32 {
        let mut ans = 0;

        for target in 0.. k {
            let mut dp = vec![0; k as usize];
            for &num in &nums {
                let m = num % k;
                let req = (target - m + k) % k;
                dp[m as usize] = dp[req as usize] + 1;
                ans = ans.max(dp[m as usize]);
            }
        }

        ans
    }
}

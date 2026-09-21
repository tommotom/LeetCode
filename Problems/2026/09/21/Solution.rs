impl Solution {
    pub fn result_array(nums: Vec<i32>, k: i32) -> Vec<i64> {
        let n = nums.len();
        let k = k as usize;
        let mut ans = vec![0i64; k];
        let mut dp = vec![0i64; k];

        for i in 0..n {
            let mut ndp = vec![0i64; k];
            ndp[(nums[i] as usize) % k] += 1;
            for r in 0..k {
                ndp[((r as i64 * nums[i] as i64) % k as i64) as usize] += dp[r];
            }
            dp = ndp;
            for r in 0..k {
                ans[r] += dp[r];
            }
        }

        ans
    }
}

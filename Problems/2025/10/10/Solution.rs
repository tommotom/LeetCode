impl Solution {
    pub fn maximum_energy(energy: Vec<i32>, k: i32) -> i32 {
        let n = energy.len();
        let k: usize = k as usize;
        let mut dp = vec![0; n];
        let mut ans = i32::MIN;
        for i in (0..n).rev() {
            dp[i] += energy[i];
            ans = ans.max(dp[i]);
            if i >= k {
                dp[i-k] = dp[i];
            }
        }
        ans
    }
}

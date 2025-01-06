impl Solution {
    pub fn count_good_strings(low: i32, high: i32, zero: i32, one: i32) -> i32 {
        const MODULO: i32 = 1_000_000_007;

        let mut dp = vec![0; (high + 1) as usize];
        dp[0] = 1;

        for i in 0..dp.len() {
            if i >= zero as usize {
                dp[i] = (dp[i] + dp[i - zero as usize]) % MODULO;
            }
            if i >= one as usize {
                dp[i] = (dp[i] + dp[i - one as usize]) % MODULO;
            }
        }

        dp[low as usize..=(high as usize)].iter().fold(0, |acc, &x| (acc + x) % MODULO)
    }
}

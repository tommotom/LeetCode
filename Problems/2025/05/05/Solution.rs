impl Solution {
    pub fn num_tilings(n: i32) -> i32 {
        let modulo = 1000000007;
        if n <= 1 {
            return 1;
        } else if n == 2 {
            return 2;
        } else if n == 3 {
            return 5;
        }
        let mut dp = vec![0; (n+1) as usize];
        dp[0] = 1;
        dp[1] = 1;
        dp[2] = 2;
        dp[3] = 5;
        for i in 4..(n+1) as usize {
            dp[i] = (dp[i-1] * 2 % modulo + dp[i-3]) % modulo;
        }
        dp[n as usize]
    }
}

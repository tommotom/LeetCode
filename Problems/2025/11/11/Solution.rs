impl Solution {
    pub fn find_max_form(strs: Vec<String>, m: i32, n: i32) -> i32 {
        let mut dp = vec![vec![0; (n + 1) as usize]; (m+1) as usize];

        fn count_zero_one(s: &str) -> (i32, i32) {
            let zeros = s.chars().filter(|&c| c == '0').count() as i32;
            let ones = s.len() as i32 - zeros;
            (zeros, ones)
        }
        let mut strs: Vec<(i32, i32)> = strs.iter().map(|s| count_zero_one(s)).collect();

        for s in strs {
            for i in (s.0..=m).rev() {
                for j in (s.1..=n).rev() {
                    dp[i as usize][j as usize] = dp[i as usize][j as usize].max(dp[(i-s.0) as usize][(j-s.1) as usize] + 1);
                }
            }
        }
        dp[m as usize][n as usize]
    }
}

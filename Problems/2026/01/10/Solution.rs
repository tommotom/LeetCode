impl Solution {
    pub fn minimum_delete_sum(s1: String, s2: String) -> i32 {
        let s1: Vec<i32> = s1.chars().map(|c| c.to_ascii_lowercase() as u8 as i32).collect();
        let s2: Vec<i32> = s2.chars().map(|c| c.to_ascii_lowercase() as u8 as i32).collect();
        let (n1, n2) = (s1.len(), s2.len());
        let mut dp = vec![vec![0; n2+1]; n1+1];
        for i1 in 1..=n1 {
            for i2 in 1..=n2 {
                if s1[i1-1] == s2[i2-1] {
                    dp[i1][i2] = dp[i1-1][i2-1] + s1[i1-1];
                } else {
                    dp[i1][i2] = dp[i1-1][i2].max(dp[i1][i2-1]);
                }
            }
        }
        let mut ans = s1.iter().sum::<i32>() + s2.iter().sum::<i32>();

        ans - 2 * dp[n1][n2]
    }
}

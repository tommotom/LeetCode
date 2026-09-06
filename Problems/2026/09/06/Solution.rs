impl Solution {
    pub fn num_distinct(s: String, t: String) -> i32 {
        let mut dp = vec![vec![0; s.len() + 1]; t.len() + 1];
        for j in 0..s.len() {
            dp[0][j] = 1;
        }
        let s: Vec<char> = s.chars().collect();
        let t: Vec<char> = t.chars().collect();
        for i in 0..t.len() {
            for j in 0..s.len() {
                if j > 0 {
                    dp[i+1][j+1] += dp[i+1][j];
                }
                if s[j] == t[i] {
                    dp[i+1][j+1] += dp[i][j];
                }
            }
        }
        dp[t.len()][s.len()]
    }
}

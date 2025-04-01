impl Solution {
    pub fn most_points(questions: Vec<Vec<i32>>) -> i64 {
        let mut dp: Vec<i64> = vec![0; questions.len()+1];
        for i in 0..questions.len() {
            dp[i+1] = dp[i+1].max(dp[i]);
            let j = questions.len().min(i + 1 + questions[i][1] as usize);
            dp[j] = dp[j].max(dp[i] + questions[i][0] as i64);
        }
        dp[questions.len()]
    }
}

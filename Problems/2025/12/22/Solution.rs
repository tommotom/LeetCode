impl Solution {
    pub fn min_deletion_size(strs: Vec<String>) -> i32 {
        let strs: Vec<Vec<char>> = strs.into_iter().map(|s| s.chars().collect()).collect();
        let n = strs[0].len();
        let mut dp = vec![1; n];
        for i in (0..n-1).rev() {
            for j in (i+1)..n {
                let mut b = false;
                for s in &strs {
                    if s[i] > s[j] {
                        b = true;
                        break;
                    }
                }
                if !b {
                    dp[i] = dp[i].max(1 + dp[j]);
                }
            }
        }
        let mut kept = 0;
        for x in dp {
            kept = kept.max(x);
        }
        (n - kept) as i32
    }
}

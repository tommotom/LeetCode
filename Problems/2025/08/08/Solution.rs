impl Solution {
    pub fn soup_servings(n: i32) -> f64 {
        if n <= 0 { return 0.5; }
        let m = ((n + 24) / 25) as usize;
        if m >= 192 { return 1.0; }

        let mut dp = vec![vec![0.0f64; m + 1]; m + 1];
        dp[0][0] = 0.5;
        for k in 1..=m {
            dp[0][k] = 1.0;
            dp[k][0] = 0.0;
        }

        let s = |x: isize| -> usize { if x <= 0 { 0 } else { x as usize } };

        for i in 1..=m {
            for j in 1..=m {
                dp[i][j] = 0.25 * (
                    dp[s(i as isize - 4)][j] +
                        dp[s(i as isize - 3)][s(j as isize - 1)] +
                        dp[s(i as isize - 2)][s(j as isize - 2)] +
                        dp[s(i as isize - 1)][s(j as isize - 3)]
                );
            }
            if dp[i][i] > 1.0 - 1e-5 {
                return 1.0;
            }
        }
        dp[m][m]
    }
}

impl Solution {
    pub fn max_path_score(grid: Vec<Vec<i32>>, k: i32) -> i32 {
        let (m, n) = (grid.len(), grid[0].len());
        let mut dp = vec![vec![vec![-1; (k+1) as usize]; n]; m];
        if grid[0][0] == 1 {
            dp[0][0][1] = 1;
        } else if grid[0][0] == 2 {
            dp[0][0][1] = 2;
        } else {
            dp[0][0][0] = 0;
        }
        for r in 0..m {
            for c in 0..n {
                if r == 0 && c == 0 {
                    continue;
                }
                let cost = if grid[r][c] > 0 {1} else {0};
                for w in cost..(k as usize + 1) {
                    let target = w - cost as usize;
                    if r > 0 && dp[r-1][c][target] > -1 {
                        dp[r][c][w] = dp[r][c][w].max(dp[r-1][c][target] + grid[r][c]);
                    }
                    if c > 0 && dp[r][c-1][target] > -1 {
                        dp[r][c][w] = dp[r][c][w].max(dp[r][c-1][target] + grid[r][c]);
                    }

                }
            }
        }
        *dp[m-1][n-1].iter().max().unwrap()
    }
}

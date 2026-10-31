impl Solution {
    pub fn unique_paths(grid: Vec<Vec<i32>>) -> i32 {
        const MOD: i32 = 1_000_000_007;
        let (m, n) = (grid.len(), grid[0].len());

        let mut f = vec![vec![[0, 0]; n]; m];
        f[0][0][0] = 1;

        for i in 0..m {
            for j in 0..n {
                if i > 0 {
                    if grid[i - 1][j] == 0 {
                        f[i][j][0] = (f[i - 1][j][0] + f[i - 1][j][1]) % MOD;
                    } else {
                        f[i][j][0] = f[i - 1][j][1];
                    }
                }

                if j > 0 {
                    if grid[i][j - 1] == 0 {
                        f[i][j][1] = (f[i][j - 1][0] + f[i][j - 1][1]) % MOD;
                    } else {
                        f[i][j][1] = f[i][j - 1][0];
                    }
                }
            }
        }

        (f[m - 1][n - 1][0] + f[m - 1][n - 1][1]) % MOD
    }
}

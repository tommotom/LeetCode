impl Solution {
    pub fn max_product_path(grid: Vec<Vec<i32>>) -> i32 {
        let m = grid.len();
        let n = grid[0].len();
        let modulo = 1_000_000_007i64;

        let mut maxdp = vec![0i64; n];
        let mut mindp = vec![0i64; n];

        maxdp[0] = grid[0][0] as i64;
        mindp[0] = grid[0][0] as i64;

        for j in 1..n {
            maxdp[j] = maxdp[j - 1] * (grid[0][j] as i64);
            mindp[j] = mindp[j - 1] * (grid[0][j] as i64);
        }

        for i in 1..m {
            maxdp[0] *= grid[i][0] as i64;
            mindp[0] *= grid[i][0] as i64;

            for j in 1..n {
                let val = grid[i][j] as i64;

                let prevmax = maxdp[j].max(maxdp[j - 1]);
                let prevmin = mindp[j].min(mindp[j - 1]);

                if val >= 0 {
                    maxdp[j] = prevmax * val;
                    mindp[j] = prevmin * val;
                } else {
                    maxdp[j] = prevmin * val;
                    mindp[j] = prevmax * val;
                }
            }
        }

        let ans = maxdp[n - 1];
        if ans < 0 {
            -1
        } else {
            (ans % modulo) as i32
        }
    }
}

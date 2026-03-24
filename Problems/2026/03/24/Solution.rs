impl Solution {
    pub fn construct_product_matrix(grid: Vec<Vec<i32>>) -> Vec<Vec<i32>> {
        let n = grid.len();
        let m = grid[0].len();
        let mut p = vec![vec![0; m]; n];
        const MOD: i64 = 12345;

        let mut suffix: i64 = 1;
        for r in (0..n).rev() {
            for c in (0..m).rev() {
                p[r][c] = suffix as i32;
                suffix = (suffix * grid[r][c] as i64) % MOD;
            }
        }

        let mut prefix: i64 = 1;
        for r in 0..n {
            for c in 0..m {
                p[r][c] = ((p[r][c] as i64 * prefix) % MOD) as i32;
                prefix = (prefix * grid[r][c] as i64) % MOD;
            }
        }

        p
    }
}

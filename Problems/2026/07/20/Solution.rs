impl Solution {
    pub fn shift_grid(grid: Vec<Vec<i32>>, k: i32) -> Vec<Vec<i32>> {
        fn shift(grid: Vec<Vec<i32>>) -> Vec<Vec<i32>> {
            let (m, n) = (grid.len(), grid[0].len());
            let mut ret = vec![vec![0; n]; m];
            ret[0][0] = grid[m-1][n-1];
            for r in 0..(m-1) {
                ret[r+1][0] = grid[r][n-1];
            }
            for r in 0..m {
                for c in 0..(n-1) {
                    ret[r][c+1] = grid[r][c];
                }
            }
            ret
        }
        let mut ret = grid.clone();
        for _ in 0..k {
            ret = shift(ret);
        }
        ret
    }
}

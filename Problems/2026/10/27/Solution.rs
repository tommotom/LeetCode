impl Solution {
    pub fn create_grid(m: i32, n: i32) -> Vec<String> {
        let (m, n) = (m as usize, n as usize);
        let mut grid = vec![vec!['#'; n]; m];
        for c in 0..n {
            grid[0][c] = '.';
        }
        for r in 0..m {
            grid[r][n-1] = '.';
        }
        grid.iter().map(|row| row.iter().collect()).collect()
    }
}

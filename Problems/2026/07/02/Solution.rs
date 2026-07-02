impl Solution {
    pub fn find_safe_walk(grid: Vec<Vec<i32>>, health: i32) -> bool {
        let (m, n) = (grid.len(), grid[0].len());
        let mut dp = vec![vec![0; n]; m];
        fn dfs(dp: &mut Vec<Vec<i32>>, grid: &Vec<Vec<i32>>, r: usize, c: usize, mut h: i32) {
            if grid[r][c] == 1 {
                h -= 1;
            }
            if dp[r][c] >= h {
                return;
            }
            dp[r][c] = h;
            if r > 0 {
                dfs(dp, grid, r-1, c, h);
            }
            if c > 0 {
                dfs(dp, grid, r, c-1, h);
            }
            if r + 1 < dp.len() {
                dfs(dp, grid, r+1, c, h);
            }
            if c + 1 < dp[0].len() {
                dfs(dp, grid, r, c+1, h);
            }
        }
        dfs(&mut dp, &grid, 0, 0, health);
        dp[m-1][n-1] > 0
    }
}

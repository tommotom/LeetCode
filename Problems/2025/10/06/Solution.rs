impl Solution {
    pub fn swim_in_water(grid: Vec<Vec<i32>>) -> i32 {
        fn helper(r: usize, c: usize, next_r: usize, next_c: usize, grid: &Vec<Vec<i32>>, dp: &mut Vec<Vec<i32>>) {
            let candidate = if grid[r][c] >= grid[next_r][next_c] {dp[r][c]} else {dp[r][c].max(grid[next_r][next_c])};
            if dp[next_r][next_c] > candidate {
                dp[next_r][next_c] = candidate;
                dfs(next_r, next_c, grid, dp);
            }
        }

        fn dfs(r: usize, c: usize, grid: &Vec<Vec<i32>>, dp: &mut Vec<Vec<i32>>) {
            if r > 0 {
                helper(r, c, r-1, c, grid, dp);
            }
            if c > 0 {
                helper(r, c, r, c-1, grid, dp);
            }
            if r+1 < grid.len() {
                helper(r, c, r+1, c, grid, dp);
            }
            if c+1 < grid.len() {
                helper(r, c, r, c+1, grid, dp);
            }
        }

        let n = grid.len();
        let mut dp = vec![vec![i32::MAX; n]; n];
        dp[0][0] = grid[0][0];
        dfs(0, 0, &grid, &mut dp);

        dp[n-1][n-1]
    }
}

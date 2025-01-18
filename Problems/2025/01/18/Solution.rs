impl Solution {
    fn is_in_cell(grid: &Vec<Vec<i32>>, r: usize, c: usize) -> bool {
        return 0 <= r && r < grid.len() && 0 <= c && c < grid[0].len();
    }

    fn dfs(mut grid: &mut Vec<Vec<i32>>, r: usize, c: usize, cost: i32, mut dp: &mut Vec<Vec<i32>>, dir: [[i32; 2]; 4]) {
        if !Self::is_in_cell(grid, r, c) {
            return;
        }
        if dp[r][c] <= cost {
            return;
        }
        dp[r][c] = cost;

        let g = grid[r][c] as usize;
        Self::dfs(grid, r + dir[g-1][0] as usize, c + dir[g-1][1] as usize, cost, dp, dir);
        for d in 0..4 {
            grid[r][c] = d as i32;
            let next_r = r + dir[d][0] as usize;
            let next_c = c + dir[d][1] as usize;
            Self::dfs(grid, next_r, next_c, cost + 1, dp, dir);
        }
        grid[r][c] = g as i32;
    }

    pub fn min_cost(mut grid: Vec<Vec<i32>>) -> i32 {
        let m = grid.len();
        let n = grid[0].len();
        let mut dp = vec![vec![999999999; n]; m];
        let dir = [[0, 1], [0, -1], [1, 0], [-1, 0]];
        Self::dfs(&mut grid, 0, 0, 0, &mut dp, dir);
        dp[m-1][n-1]
    }
}

impl Solution {
    pub fn closed_island(mut grid: Vec<Vec<i32>>) -> i32 {
        fn dfs(grid: &mut Vec<Vec<i32>>, r: usize, c: usize) {
            grid[r][c] = 1;
            if r > 0 && grid[r-1][c] == 0 {
                dfs(grid, r-1, c);
            }
            if c > 0 && grid[r][c-1] == 0 {
                dfs(grid, r, c-1);
            }
            if r + 1 < grid.len() && grid[r+1][c] == 0 {
                dfs(grid, r+1, c);
            }
            if c + 1 < grid[0].len() && grid[r][c+1] == 0 {
                dfs(grid, r, c+1);
            }
        }

        let (m, n) = (grid.len(), grid[0].len());

        let mut ans = 0;
        for r in 0..m {
            if grid[r][0] == 0 {
                dfs(&mut grid, r, 0);
            }
            if grid[r][n-1] == 0 {
                dfs(&mut grid, r, n-1);
            }
        }
        for c in 0..n {
            if grid[0][c] == 0 {
                dfs(&mut grid, 0, c);
            }
            if grid[m-1][c] == 0 {
                dfs(&mut grid, m-1, c);
            }
        }
        for r in 0..m {
            for c in 0..n {
                if grid[r][c] == 0 {
                    dfs(&mut grid, r, c);
                    ans += 1;
                }
            }
        }
        ans
    }
}

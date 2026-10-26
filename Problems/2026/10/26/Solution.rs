impl Solution {
    pub fn count_islands(mut grid: Vec<Vec<i32>>, k: i32) -> i32 {
        fn dfs(grid: &mut Vec<Vec<i32>>, r: usize, c: usize) -> i64 {
            let mut ret = grid[r][c] as i64;
            grid[r][c] = 0;
            if r > 0 && grid[r-1][c] > 0 {
                ret += dfs(grid, r-1, c);
            }
            if c > 0 && grid[r][c-1] > 0 {
                ret += dfs(grid, r, c-1);
            }
            if r + 1 < grid.len() && grid[r+1][c] > 0 {
                ret += dfs(grid, r+1, c);
            }
            if c + 1 < grid[0].len() && grid[r][c+1] > 0 {
                ret += dfs(grid, r, c+1);
            }
            ret
        }
        let k = k as i64;
        let mut ans = 0;
        for r in 0..grid.len() {
            for c in 0..grid[0].len() {
                if grid[r][c] > 0 {
                    let mut sum = dfs(&mut grid, r, c);
                    if sum % k == 0 {
                        ans += 1;
                    }
                }
            }
        }
        ans
    }
}

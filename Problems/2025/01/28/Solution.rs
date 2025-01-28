impl Solution {
    pub fn find_max_fish(mut grid: Vec<Vec<i32>>) -> i32 {
        fn dfs(grid: &mut Vec<Vec<i32>>, r: usize, c: usize) -> i32 {
            let mut fish = grid[r][c];
            grid[r][c] = 0;
            let adj = [(0, 1), (0, -1), (1, 0), (-1, 0)];
            for (dr, dc) in adj {
                let next_r = r as i32 + dr;
                let next_c = c as i32 + dc;
                if next_r < 0 || next_r == grid.len() as i32 || next_c < 0 || next_c == grid[0].len() as i32 || grid[next_r as usize][next_c as usize] == 0 {
                    continue;
                }
                fish += dfs(grid, next_r as usize, next_c as usize);
            }
            fish
        }

        let mut ans = 0;
        for r in 0..grid.len() {
            for c in 0.. grid[0].len() {
                if grid[r][c] > 0 {
                    ans = ans.max(dfs(&mut grid, r, c));
                }
            }
        }

        ans
    }
}

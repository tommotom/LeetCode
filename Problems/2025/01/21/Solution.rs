impl Solution {
    pub fn grid_game(grid: Vec<Vec<i32>>) -> i64 {
        let mut first: i64 = grid[0].iter().map(|a| *a as i64).sum();
        let mut second: i64 = 0;
        let mut ans = i64::MAX;
        for i in 0..grid[0].len() {
            first -= grid[0][i] as i64;
            ans = ans.min(first.max(second));
            second += grid[1][i] as i64;
        }
        ans
    }
}

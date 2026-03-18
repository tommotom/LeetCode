impl Solution {
    pub fn count_submatrices(grid: Vec<Vec<i32>>, k: i32) -> i32 {
        let m = grid.len();
        let n = grid[0].len();
        let mut cum: Vec<Vec<i32>> = Vec::new();
        for r in 0..m {
            let mut row = vec![grid[r][0]];
            for c in 1..n {
                row.push(row[c-1] + grid[r][c]);
            }
            cum.push(row);
        }
        let mut ans = 0;
        for c in 0..n {
            let mut sum = 0;
            for r in 0..m {
                sum += cum[r][c];
                if sum > k {
                    break;
                }
                ans += 1;
            }
        }
        ans
    }
}

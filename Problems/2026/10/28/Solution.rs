impl Solution {
    pub fn min_cost(grid: Vec<Vec<i32>>) -> i32 {
        let (m, n) = (grid.len(), grid[0].len());
        let mut dp = vec![vec![vec![false; 1024]; n]; m];
        dp[0][0][grid[0][0] as usize] = true;
        for r in 0..m {
            for c in 0..n {
                if r == 0 && c == 0 {
                    continue;
                }
                for num in 0..1024 {
                    if r > 0 && dp[r-1][c][num] {
                        let xor = (num as i32) ^ grid[r][c];
                        dp[r][c][xor as usize] = true;
                    }
                    if c > 0 && dp[r][c-1][num] {
                        let xor = (num as i32) ^ grid[r][c];
                        dp[r][c][xor as usize] = true;
                    }
                }
            }
        }
        for num in 0..1024 {
            if dp[m-1][n-1][num] {
                return num as i32;
            }
        }
        0
    }
}

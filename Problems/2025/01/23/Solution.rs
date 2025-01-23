impl Solution {
    pub fn count_servers(grid: Vec<Vec<i32>>) -> i32 {
        let m = grid.len();
        let n = grid[0].len();
        let mut row_count = vec![0; m];
        let mut col_count = vec![0; n];
        let mut computers = 0;
        for r in 0..m {
            for c in 0..n {
                if grid[r][c] == 1 {
                    row_count[r] += 1;
                    col_count[c] += 1;
                    computers += 1;
                }
            }
        }

        let mut independent = 0;
        for r in 0..m {
            for c in 0..n {
                if grid[r][c] == 1 && row_count[r] == 1 && col_count[c] == 1 {
                    independent += 1;
                }
            }
        }

        computers - independent
    }
}

impl Solution {
    pub fn count_servers(grid: Vec<Vec<i32>>) -> i32 {
        let row_count: Vec<i32> = grid.iter().map(|row| row.iter().sum::<i32>()).collect();
        let mut col_count = Vec::new();
        for c in 0..grid[0].len() {
            let mut count = 0;
            for r in 0..grid.len() {
                count += grid[r][c];
            }
            col_count.push(count);
        }

        let servers: i32 = grid.iter().map(|row| row.iter().sum::<i32>()).sum();
        let mut cannot = 0;
        for r in 0..grid.len() {
            for c in 0..grid[0].len() {
                if grid[r][c] == 1 && row_count[r] == 1 && col_count[c] == 1 {
                    cannot += 1
                }
            }
        }
        servers - cannot
    }
}

impl Solution {
    pub fn number_of_submatrices(grid: Vec<Vec<char>>) -> i32 {
        let mut x: Vec<Vec<i32>> = Vec::new();
        let mut y: Vec<Vec<i32>> = Vec::new();
        let m = grid.len();
        let n = grid[0].len();
        for r in 0..m {
            let mut x_r = Vec::new();
            let mut y_r = Vec::new();
            let mut x_c = 0;
            let mut y_c = 0;
            for c in 0..n {
                if grid[r][c] == 'X' {
                    x_c += 1;
                } else if grid[r][c] == 'Y' {
                    y_c += 1;
                }
                x_r.push(x_c);
                y_r.push(y_c);
            }
            x.push(x_r);
            y.push(y_r);
        }
        let mut ans = 0;
        for c in 0..n {
            let mut x_c = 0;
            let mut y_c = 0;
            for r in 0..m {
                x_c += x[r][c];
                y_c += y[r][c];
                if x_c > 0 && x_c == y_c {
                    ans += 1;
                }
            }
        }
        ans
    }
}

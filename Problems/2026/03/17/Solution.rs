impl Solution {
    pub fn largest_submatrix(matrix: Vec<Vec<i32>>) -> i32 {
        let m = matrix.len();
        let n = matrix[0].len();
        let mut con: Vec<Vec<i32>> = Vec::new();
        for r in 0..m {
            let mut row = Vec::new();
            for c in 0..n {
                if matrix[r][c] == 0 {
                    row.push(0);
                } else if r > 0 && matrix[r-1][c] == 1 {
                    row.push(con[r-1][c] + 1);
                } else {
                    row.push(1);
                }
            }
            con.push(row);
        }
        let mut ans = 0;
        for r in 0..m {
            con[r].sort_by(|a, b| b.cmp(a));
            for c in 0..n {
                ans = ans.max((c as i32 + 1) * con[r][c]);
            }
        }
        ans
    }
}

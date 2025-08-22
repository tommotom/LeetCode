impl Solution {
    pub fn num_submat(mat: Vec<Vec<i32>>) -> i32 {
        let m = mat.len();
        let n = mat[0].len();
        let mut res = 0;
        let mut row = vec![vec![0; n]; m];

        for i in 0..m {
            for j in 0..n {
                row[i][j] = if j == 0 {
                    mat[i][j]
                } else {
                    if mat[i][j] == 0 { 0 } else { row[i][j - 1] + 1 }
                };
                let mut cur = row[i][j];
                for k in (0..=i).rev() {
                    cur = cur.min(row[k][j]);
                    if cur == 0 {
                        break;
                    }
                    res += cur;
                }
            }
        }
        res
    }
}

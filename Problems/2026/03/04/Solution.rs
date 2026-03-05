impl Solution {
    pub fn num_special(mat: Vec<Vec<i32>>) -> i32 {
        let mut row_count = Vec::new();
        for r in 0..mat.len() {
            let mut count = 0;
            for c in 0..mat[0].len() {
                count += mat[r][c];
            }
            row_count.push(count);
        }

        let mut col_count = Vec::new();
        for c in 0..mat[0].len() {
            let mut count = 0;
            for r in 0..mat.len() {
                count += mat[r][c];
            }
            col_count.push(count);
        }

        let mut ans = 0;
        for r in 0..mat.len() {
            for c in 0..mat[0].len() {
                if mat[r][c] == 1 && row_count[r] == 1 && col_count[c] == 1 {
                    ans += 1;
                }
            }
        }
        ans
    }
}

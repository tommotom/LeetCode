impl Solution {
    pub fn rotate(matrix: &mut Vec<Vec<i32>>) {
        let mut d = 0;
        let n = matrix.len();
        for d in 0..(n/2) {
            for c in d..(n-1-d) {
                let tmp = matrix[d][c];
                matrix[d][c] = matrix[n-c-1][d];
                matrix[n-c-1][d] = matrix[n-d-1][n-c-1];
                matrix[n-d-1][n-c-1] = matrix[c][n-d-1];
                matrix[c][n-d-1] = tmp;
            }
        }
    }
}

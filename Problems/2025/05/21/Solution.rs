impl Solution {
    pub fn set_zeroes(matrix: &mut Vec<Vec<i32>>) {
        let mut is_first_row_zero = false;
        for j in 0..matrix[0].len() {
            if matrix[0][j] == 0 {
                is_first_row_zero = true;
            }
        }

        let mut is_first_col_zero = false;
        for i in 0..matrix.len() {
            if matrix[i][0] == 0 {
                is_first_col_zero = true;
            }
        }

        for i in 1..matrix.len() {
            for j in 1..matrix[0].len() {
                if matrix[i][j] == 0 {
                    matrix[i][0] = 0;
                    matrix[0][j] = 0;
                }
            }
        }

        for i in 1..matrix.len() {
            for j in 1..matrix[0].len() {
                if matrix[i][0] == 0 || matrix[0][j] == 0 {
                    matrix[i][j] = 0;
                }
            }
        }

        if is_first_row_zero {
            for j in 0..matrix[0].len() {
                matrix[0][j] = 0;
            }
        }

        if is_first_col_zero {
            for i in 0..matrix.len() {
                matrix[i][0] = 0;
            }
        }
    }
}

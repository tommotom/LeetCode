impl Solution {
    pub fn max_matrix_sum(matrix: Vec<Vec<i32>>) -> i64 {
        let mut sum: i64 = 0;
        let mut min = i64::MAX;
        let mut count = 0;
        for row in matrix {
            for num in row {
                sum += num.abs() as i64;
                min = min.min(num.abs() as i64);
                count += if num < 0 {1} else {0};
            }
        }
        if count % 2 == 0 {sum} else {sum - 2 * min}
    }
}

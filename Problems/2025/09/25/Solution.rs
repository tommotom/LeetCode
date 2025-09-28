impl Solution {
    pub fn minimum_total(mut triangle: Vec<Vec<i32>>) -> i32 {
        for row in 1..triangle.len() {
            for col in 0..triangle[row].len() {
                let mut num = i32::MAX;
                if col > 0 {
                    num = num.min(triangle[row-1][col-1]);
                }
                if col < triangle[row-1].len() {
                    num = num.min(triangle[row-1][col]);
                }
                triangle[row][col] += num;
            }
        }
        *triangle[triangle.len()-1].iter().min().unwrap()
    }
}

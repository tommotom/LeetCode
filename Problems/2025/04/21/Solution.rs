impl Solution {
    pub fn number_of_arrays(differences: Vec<i32>, lower: i32, upper: i32) -> i32 {
        let mut min = 0;
        let mut max = 0;
        let mut sum = 0;
        for num in differences {
            sum += num as i64;
            min = min.min(sum);
            max = max.max(sum);
        }
        ((upper - lower) - (max - min) as i32 + 1).max(0)
    }
}

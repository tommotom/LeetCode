impl Solution {
    pub fn max_total_value(nums: Vec<i32>, k: i32) -> i64 {
        let min = nums.iter().min().unwrap();
        let max = nums.iter().max().unwrap();
        (max - min) as i64 * k as i64
    }
}

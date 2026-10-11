impl Solution {
    pub fn sum_of_squares(nums: Vec<i32>) -> i32 {
        let n = nums.len();
        nums.into_iter().enumerate().filter(|(i, x)| n % (*i + 1) == 0).map(|(i, x)| x * x).sum()
    }
}

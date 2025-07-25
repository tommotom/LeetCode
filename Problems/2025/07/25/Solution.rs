use std::collections::HashSet;

impl Solution {
    pub fn max_sum(nums: Vec<i32>) -> i32 {
        let max = nums.clone().into_iter().max().unwrap();
        let nums: HashSet<i32> = nums.into_iter().filter(|x| *x > 0).collect();
        if nums.len() == 0 {
            return max
        }
        nums.into_iter().sum::<i32>()
    }
}

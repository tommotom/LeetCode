use std::collections::HashSet;

impl Solution {
    pub fn find_final_value(nums: Vec<i32>, mut original: i32) -> i32 {
        let nums: HashSet<i32> = nums.iter().cloned().collect();
        while nums.contains(&original) {
            original *= 2;
        }
        original
    }
}

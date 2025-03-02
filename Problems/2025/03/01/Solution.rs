use std::cmp::Ordering;

impl Solution {
    pub fn apply_operations(mut nums: Vec<i32>) -> Vec<i32> {
        for i in 0..nums.len()-1 {
            if nums[i] == nums[i+1] {
                nums[i] *= 2;
                nums[i+1] = 0;
            }
        }
        nums.sort_by(|a, b| if *b == 0 {Ordering::Less} else {Ordering::Equal});
        nums
    }
}

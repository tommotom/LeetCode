impl Solution {
    pub fn target_indices(mut nums: Vec<i32>, target: i32) -> Vec<i32> {
        nums.sort();
        nums.into_iter().enumerate().filter(|(i, x)| *x == target).map(|(i, x)| i as i32).collect()
    }
}

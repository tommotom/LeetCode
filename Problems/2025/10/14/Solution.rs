impl Solution {
    pub fn has_increasing_subarrays(nums: Vec<i32>, k: i32) -> bool {
        fn is_increasing(nums: &Vec<i32>, start: usize, k: usize) -> bool {
            for i in start..(start+k-1) {
                if nums[i] >= nums[i+1] {
                    return false;
                }
            }
            true
        }
        let k: usize = k as usize;
        for i in 0..(nums.len() - 2 * k + 1) {
            if is_increasing(&nums, i, k) && is_increasing(&nums, i + k, k) {
                return true;
            }
        }
        false
    }
}

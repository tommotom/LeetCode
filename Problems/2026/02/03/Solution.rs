impl Solution {
    pub fn is_trionic(nums: Vec<i32>) -> bool {
        let mut i = 0;
        if nums[i] >= nums[i+1] {
            return false;
        }
        while i + 1 < nums.len() && nums[i] < nums[i+1] {
            i += 1;
        }
        if i + 1 == nums.len() || nums[i] <= nums[i+1] {
            return false;
        }
        while i + 1 < nums.len() && nums[i] > nums[i+1] {
            i += 1;
        }
        if i + 1 == nums.len() || nums[i] >= nums[i+1] {
            return false;
        }
        while i + 1 < nums.len() && nums[i] < nums[i+1] {
            i += 1;
        }
        i + 1 == nums.len()
    }
}

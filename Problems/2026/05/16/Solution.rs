impl Solution {
    pub fn find_min(nums: Vec<i32>) -> i32 {
        let (mut i, mut j) = (0, nums.len() - 1);
        if nums[i] < nums[j] || j == 0 {
            return nums[i];
        }

        while i < j {
            if nums[i] > nums[j] {
                i += 1;
            } else {
                j -= 1;
            }
        }

        nums[j]
    }
}

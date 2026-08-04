impl Solution {
    pub fn find_missing_elements(mut nums: Vec<i32>) -> Vec<i32> {
        nums.sort();
        let mut i = 0;
        let mut missing = Vec::new();
        for num in nums[0]..=nums[nums.len()-1] {
            if nums[i] == num {
                i += 1;
            } else {
                missing.push(num);
            }
        }
        missing
    }
}

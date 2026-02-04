impl Solution {
    pub fn minimum_cost(nums: Vec<i32>) -> i32 {
        let a = nums[0];
        let mut nums: Vec<&i32> = nums.iter().skip(1).collect();
        nums.sort();
        a + nums[0] + nums[1]
    }
}

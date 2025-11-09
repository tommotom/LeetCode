impl Solution {
    pub fn max_adjacent_distance(nums: Vec<i32>) -> i32 {
        let mut ans = (nums[0] - nums[nums.len() - 1]).abs();
        for i in 1..nums.len() {
            ans = ans.max((nums[i-1] - nums[i]).abs());
        }
        ans
    }
}

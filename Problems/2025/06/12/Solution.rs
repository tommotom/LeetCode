impl Solution {
    pub fn max_adjacent_distance(nums: Vec<i32>) -> i32 {
        let n = nums.len();
        let mut ans = (nums[0] - nums[n-1]).abs();
        for i in 1..n {
            ans = ans.max((nums[i] - nums[i-1]).abs());
        }
        ans
    }
}

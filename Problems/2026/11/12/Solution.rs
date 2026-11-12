impl Solution {
    pub fn longest_monotonic_subarray(nums: Vec<i32>) -> i32 {
        let mut increasing = 1;
        let mut decreasing = 1;
        let mut ans = 1;
        for i in 1..nums.len() {
            if nums[i-1] < nums[i] {
                increasing += 1;
                decreasing = 1;
            } else if nums[i-1] > nums[i] {
                decreasing += 1;
                increasing = 1;
            } else {
                increasing = 1;
                decreasing = 1;
            }
            ans = ans.max(increasing).max(decreasing);
        }
        ans
    }
}

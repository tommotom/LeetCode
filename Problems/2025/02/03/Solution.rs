impl Solution {
    pub fn longest_monotonic_subarray(nums: Vec<i32>) -> i32 {
        let mut inc = 1;
        let mut dec = 1;
        let mut ans = 1;
        for i in 1..nums.len() {
            if nums[i-1] < nums[i] {
                inc += 1;
            } else {
                inc = 1;
            }
            if nums[i-1] > nums[i] {
                dec += 1;
            } else {
                dec = 1;
            }
            ans = ans.max(inc);
            ans = ans.max(dec);
        }
        ans as i32
    }
}

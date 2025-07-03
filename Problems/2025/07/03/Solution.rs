impl Solution {
    pub fn longest_monotonic_subarray(nums: Vec<i32>) -> i32 {
        let n = nums.len();
        let (mut inc, mut dec, mut ans) = (1, 1, 1);
        for i in 1..n {
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
            ans = ans.max(inc).max(dec);
        }
        ans
    }
}

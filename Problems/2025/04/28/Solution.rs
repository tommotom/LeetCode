impl Solution {
    pub fn count_subarrays(nums: Vec<i32>, k: i64) -> i64 {
        let mut sum = 0 as i64;
        let mut l = 0;
        let mut ans = 0;
        for r in 0..nums.len() {
            sum += nums[r] as i64;
            while l <= r && sum * (r - l + 1) as i64 >= k {
                sum -= nums[l] as i64;
                l += 1;
            }
            ans += (r - l + 1) as i64;
        }
        ans
    }
}

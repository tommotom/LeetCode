use std::collections::HashSet;

impl Solution {
    pub fn maximum_unique_subarray(nums: Vec<i32>) -> i32 {
        let mut seen = HashSet::new();
        let mut sum = 0;
        let mut r = 0;
        let mut ans = 0;
        for &num in &nums {
            while seen.contains(&num) {
                sum -= nums[r];
                seen.remove(&nums[r]);
                r += 1;
            }
            seen.insert(num);
            sum += num;
            ans = ans.max(sum);
        }
        ans
    }
}

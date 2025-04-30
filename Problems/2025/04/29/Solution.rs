use std::collections::HashMap;
use std::collections::VecDeque;

impl Solution {
    pub fn count_subarrays(nums: Vec<i32>, k: i32) -> i64 {
        let max = nums.clone().into_iter().reduce(|a, b| a.max(b)).unwrap();
        let mut l = 0;
        let mut count = 0;
        let mut ans = 0;
        for r in 0..nums.len() {
            if nums[r] == max {
                count += 1;
            }
            while count >= k {
                if nums[l] == max {
                    count -= 1;
                }
                l += 1;
            }
            ans += l as i64;
        }
        ans
    }
}

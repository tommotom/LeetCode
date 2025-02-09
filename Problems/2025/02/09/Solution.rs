use std::collections::HashMap;

impl Solution {
    pub fn count_bad_pairs(nums: Vec<i32>) -> i64 {
        let mut counter = HashMap::new();
        let mut ans = 0;
        for i in 0..nums.len() {
            let key = i as i32 - nums[i];
            ans += i as i64 - *counter.entry(key).or_insert(0);
            *counter.entry(key).or_insert(0) += 1;
        }
        ans
    }
}

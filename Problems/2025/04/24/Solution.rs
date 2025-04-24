use std::collections::HashSet;
use std::collections::HashMap;

impl Solution {
    pub fn count_complete_subarrays(nums: Vec<i32>) -> i32 {
        let mut distinct = HashSet::new();
        for num in &nums {
            distinct.insert(num);
        }
        let n = distinct.len();
        let mut counter = HashMap::new();
        let mut l = 0;
        let mut ans = 0;
        for r in 0..nums.len() {
            *counter.entry(nums[r]).or_insert(0) += 1;
            while counter.len() == n && *counter.get(&nums[l]).unwrap() > 1 {
                *counter.entry(nums[l]).or_insert(0) -= 1;
                l += 1;
            }
            if counter.len() == n {
                ans += l + 1;
            }
        }
        ans as i32
    }
}

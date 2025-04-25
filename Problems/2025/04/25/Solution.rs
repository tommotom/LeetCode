use std::collections::HashMap;

impl Solution {
    pub fn count_interesting_subarrays(nums: Vec<i32>, modulo: i32, k: i32) -> i64 {
        let mut cnt = 0;
        let mut map = HashMap::new();
        map.insert(0, 1);
        let mut ans = 0;
        for i in 0..nums.len() {
            cnt += if nums[i] % modulo == k {1} else {0};
            ans += *map.entry((cnt - k + modulo) % modulo).or_insert(0);
            *map.entry(cnt % modulo).or_insert(0) += 1;
        }
        ans
    }
}

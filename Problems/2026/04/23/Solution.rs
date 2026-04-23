use std::collections::HashMap;

impl Solution {
    pub fn distance(nums: Vec<i32>) -> Vec<i64> {
        let mut map = HashMap::new();
        for i in 0..nums.len() {
            map.entry(nums[i]).or_insert(Vec::new()).push(i as i64);
        }
        let mut ans = vec![0 as i64; nums.len()];
        for arr in map.values() {
            let mut right_sum: i64 = arr.iter().sum();
            let mut left_sum: i64 = 0;
            for (i, &val) in arr.iter().enumerate() {
                right_sum -= val;
                ans[val as usize] = (i as i64 * val - left_sum) + (right_sum - (arr.len() - i - 1) as i64 * val);
                left_sum += val;
            }
        }
        ans
    }
}

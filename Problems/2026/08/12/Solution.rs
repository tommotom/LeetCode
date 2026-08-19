use std::collections::HashMap;

impl Solution {
    pub fn max_subarray_length(nums: Vec<i32>, k: i32) -> i32 {
        let mut freq = HashMap::new();

        let mut result = 0;
        let mut left = 0;

        for (right, &num) in nums.iter().enumerate() {
            freq.entry(num).and_modify(|f| *f += 1).or_insert(1);

            while *freq.get(&num).unwrap() > k {
                *freq.get_mut(&nums[left]).unwrap() -= 1;
                left += 1;
            }

            result = result.max(right + 1 - left);
        }

        result as i32
    }
}

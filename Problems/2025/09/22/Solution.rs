use std::collections::HashMap;

impl Solution {
    pub fn max_frequency_elements(nums: Vec<i32>) -> i32 {
        let mut counter = HashMap::new();
        let (mut max_freq, mut ans) = (0, 0);
        for num in nums {
            *counter.entry(num).or_insert(0) += 1;
            let count = *counter.get(&num).unwrap();
            if count > max_freq {
                max_freq = count;
                ans = count;
            } else if count == max_freq {
                ans += count;
            }
        }
        ans
    }
}

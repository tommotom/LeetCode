use std::collections::HashMap;

impl Solution {
    pub fn find_smallest_integer(nums: Vec<i32>, value: i32) -> i32 {
        let mut counter = HashMap::new();
        for num in nums {
            if num < 0 {
                let num = (num.abs() + value - 1) / value * value + num;
                *counter.entry(num).or_insert(0) += 1;
            } else {
                let num = num - num / value * value;
                *counter.entry(num).or_insert(0) += 1;
            }
        }
        let mut ans = 0;
        loop {
            if !counter.contains_key(&ans) || *counter.get(&ans).unwrap() == 0 {
                return ans;
            }
            let count = counter.get(&ans).unwrap();
            *counter.entry(ans+value).or_insert(0) += count - 1;
            ans += 1;
        }
        0
    }
}

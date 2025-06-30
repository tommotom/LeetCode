use std::collections::HashMap;

impl Solution {
    pub fn find_lhs(nums: Vec<i32>) -> i32 {
        let mut counter = HashMap::new();
        for num in nums {
            *counter.entry(num).or_insert(0) += 1;
        }
        let mut ans = 0;
        for (num, count) in counter.iter() {
            if counter.contains_key(&(num-1)) {
                ans = ans.max(count + counter.get(&(num-1)).unwrap());
            }
            if counter.contains_key(&(num+1)) {
                ans = ans.max(count + counter.get(&(num+1)).unwrap());
            }
        }
        ans
    }
}

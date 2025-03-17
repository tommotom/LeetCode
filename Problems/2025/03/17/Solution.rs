use std::collections::HashMap;

impl Solution {
    pub fn divide_array(nums: Vec<i32>) -> bool {
        let mut counter = HashMap::new();
        for num in nums {
            *counter.entry(num).or_insert(0) += 1;
        }
        for count in counter.values() {
            if count % 2 == 1 {
                return false;
            }
        }
        true
    }
}

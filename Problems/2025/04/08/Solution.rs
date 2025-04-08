use std::collections::HashMap;
use std::collections::HashSet;

impl Solution {
    pub fn minimum_operations(nums: Vec<i32>) -> i32 {
        let mut counter = HashMap::new();
        let mut duplicated = HashSet::new();
        for num in &nums {
            *counter.entry(*num).or_insert(0) += 1;
            if counter[num] > 1 {
                duplicated.insert(*num);
            }
        }

        let mut i = 0;
        let mut operations = 0;
        while !duplicated.is_empty() {
            operations += 1;
            for j in i..(i+3).min(nums.len()) {
                if let Some(count) = counter.get_mut(&nums[j]) {
                    *count -= 1;
                    if *count <= 1 {
                        duplicated.remove(&nums[j]);
                    }
                }
            }
            i += 3;
        }
        operations
    }
}

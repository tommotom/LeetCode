use std::collections::HashMap;

impl Solution {
    pub fn special_triplets(nums: Vec<i32>) -> i32 {
        let mut left: HashMap<i32, i64> = HashMap::new();
        let mut right: HashMap<i32, i64> = HashMap::new();
        for i in 1..nums.len() {
            *right.entry(nums[i]).or_insert(0) += 1;
        }
        let mut ans: i64 = 0;
        for i in 1..(nums.len()-1) {
            *right.entry(nums[i]).or_insert(0) -= 1;
            *left.entry(nums[i-1]).or_insert(0) += 1;
            let target = nums[i] * 2;
            if !right.contains_key(&target) || *right.get(&target).unwrap() == 0 {
                continue;
            }
            if !left.contains_key(&target) || *left.get(&target).unwrap() == 0 {
                continue;
            }
            ans += *right.get(&target).unwrap() * *left.get(&target).unwrap();
            ans %= 1000000007;
        }
        ans as i32
    }
}

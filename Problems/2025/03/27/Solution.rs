use std::collections::HashMap;

impl Solution {
    pub fn minimum_index(nums: Vec<i32>) -> i32 {
        let n = nums.len();
        let mut a = HashMap::new();
        let mut b = HashMap::new();
        for num in &nums {
            *b.entry(num).or_insert(0) += 1;
        }
        let mut count = 0;
        let mut candidate = -1;
        for i in 0..nums.len()-1 {
            *a.entry(&nums[i]).or_insert(0) += 1;
            *b.entry(&nums[i]).or_insert(0) -= 1;
            if count == 0 {
                candidate = nums[i];
            }
            if candidate == nums[i] {
                count += 1;
            } else {
                count -= 1;
            }
            if *a.get(&candidate).unwrap() > (i+1) / 2  && *b.get(&candidate).unwrap()  > (n-i-1) / 2 {
                return i as i32
            }
        }
        -1
    }
}

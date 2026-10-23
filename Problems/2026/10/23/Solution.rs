use std::collections::HashMap;

impl Solution {
    pub fn sort_permutation(mut nums: Vec<i32>) -> i32 {
        let n = nums.len();
        let mut index = HashMap::new();
        for i in 0..n {
            index.insert(nums[i], i);
        }

        let mut ans = -1;
        for i in 0..nums.len() {
            if nums[i] != i as i32 {
                let j = *index.get(&(i as i32)).unwrap();
                nums[j] = nums[i];
                nums[i] = i as i32;
                index.insert(nums[i], i);
                index.insert(nums[j], j);
                let k = nums[i] & nums[j];
                ans &= k;
            }
        }
        if ans == -1 {0} else {ans}
    }
}

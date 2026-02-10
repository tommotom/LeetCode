use std::collections::HashMap;

impl Solution {
    pub fn longest_balanced(nums: Vec<i32>) -> i32 {
        let mut evens = HashMap::new();
        let mut odds = HashMap::new();
        let mut ans = 0;
        for i in 0..nums.len() {
            if nums[i] % 2 == 0 {
                *evens.entry(nums[i]).or_insert(0) += 1;
            } else {
                *odds.entry(nums[i]).or_insert(0) += 1;
            }

            let mut diff = evens.len() - odds.len();
            let mut evens_copy = evens.clone();
            let mut odds_copy = odds.clone();

            let mut j = 0;
            while j < i && evens_copy.len() != odds_copy.len() {
                if nums[j] % 2 == 0 {
                    *evens_copy.entry(nums[j]).or_insert(0) -= 1;
                    if *evens_copy.get(&nums[j]).unwrap() == 0 {
                        evens_copy.remove(&nums[j]);
                    }
                } else {
                    *odds_copy.entry(nums[j]).or_insert(0) -= 1;
                    if *odds_copy.get(&nums[j]).unwrap() == 0 {
                        odds_copy.remove(&nums[j]);
                    }
                }
                j += 1
            }
            if j < i {
                ans = ans.max(i - j + 1);
            }
        }
        ans as i32
    }
}

use std::collections::HashMap;

impl Solution {
    pub fn count_good(nums: Vec<i32>, k: i32) -> i64 {
        let mut counter = HashMap::new();
        let mut pairs = 0;
        let mut j = 0;
        let mut ans = 0;
        for i in 0..nums.len() {
            let num = nums[i];
            *counter.entry(num).or_insert(0) += 1;
            let count = counter.get(&num).unwrap();
            pairs += (count-1);
            while j < i && pairs >= k {
                let numj = nums[j];
                let countj = counter.get(&numj).unwrap();
                pairs -= (countj-1);
                counter.insert(numj, countj-1);
                j += 1;
            }
            ans += j as i64;
        }
        ans
    }
}

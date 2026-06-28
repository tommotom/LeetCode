use std::collections::HashMap;

impl Solution {
    pub fn maximum_length(nums: Vec<i32>) -> i32 {
        let mut counter = HashMap::new();
        for num in nums {
            *counter.entry(num).or_insert(0) += 1;
        }
        let mut ans = 1;
        for x in counter.keys() {
            let mut k = 1;
            let mut p = *x;
            while counter.contains_key(&p) {
                ans = ans.max((k-1) * 2 + 1);
                let count = *counter.get(&p).unwrap();
                if p == 1 {
                    ans = ans.max((count-1) / 2 * 2 + 1);
                    break;
                }
                if count == 1 {
                    break;
                }
                if ((p as i64) * (p as i64)) > (i32::MAX as i64) {
                    break;
                }
                p *= p;
                k += 1;
            }
        }
        ans
    }
}

use std::collections::HashMap;

impl Solution {
    pub fn min_subarray(nums: Vec<i32>, p: i32) -> i32 {
        let mut sum = 0;
        for i in 0..nums.len() {
            sum = (sum + nums[i]) % p;
        }
        let target = sum % p;
        if target == 0 {
            return 0;
        }
        let mut seen: HashMap<i32, i32> = HashMap::new();
        seen.insert(0, -1);
        let mut cur = 0;
        let mut ans = nums.len() as i32;
        for i in 0..nums.len() {
            cur = (cur + nums[i]) % p;
            let n = (cur - target + p) % p;
            if seen.contains_key(&n) {
                ans = ans.min(i as i32 - *seen.get(&n).unwrap());
            }
            seen.insert(cur, i as i32);
        }
        if (ans as usize) == nums.len() {-1} else {ans}
    }
}

use std::collections::VecDeque;

impl Solution {
    pub fn smallest_subarrays(nums: Vec<i32>) -> Vec<i32> {
        let mut bits = vec![VecDeque::new(); 32];
        for i in 0..nums.len() {
            for d in 0..32 {
                if (nums[i] & (1 << d)) > 0 {
                    bits[d].push_back(i);
                }
            }
        }
        let mut ans = Vec::new();
        for i in 0..nums.len() {
            let mut j = i;
            for d in 0..32 {
                while bits[d].len() > 0 && bits[d][0] < i {
                    bits[d].pop_front();
                }
                if bits[d].len() > 0 {
                    j = j.max(bits[d][0]);
                }
            }
            ans.push((j - i + 1) as i32);
        }
        ans
    }
}

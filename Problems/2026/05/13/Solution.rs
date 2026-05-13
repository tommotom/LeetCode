use std::collections::HashMap;

impl Solution {
    pub fn min_moves(mut nums: Vec<i32>, limit: i32) -> i32 {
        let n = nums.len();
        let mut diff = vec![0; (2 * limit + 2) as usize];

        for i in 0..n/2 {
            let a = nums[i].min(nums[n - i - 1]) as usize;
            let b = nums[i].max(nums[n - i - 1]) as usize;

            diff[2] += 2;
            diff[a+1] -= 1;
            diff[a+b] -= 1;
            diff[a+b+1] += 1;
            diff[b + limit as usize + 1] += 1;
        }

        let mut ans = n as i32;
        let mut cur = 0;
        for c in 2..=(2 * limit) as usize {
            cur += diff[c];
            ans = ans.min(cur);
        }
        ans
    }
}

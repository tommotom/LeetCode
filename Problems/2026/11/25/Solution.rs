use std::collections::HashMap;

impl Solution {
    pub fn smallest_unique_subarray(nums: Vec<i32>) -> i32 {
        let n = nums.len();
        if n <= 1 {
            return n as i32;
        }

        const MOD1: u64 = 1_000_000_007;
        const MOD2: u64 = 1_000_000_009;
        const BASE1: u64 = 131_071;
        const BASE2: u64 = 131_101;

        let has_unique = |len: usize| -> bool {
            let mut h1: u64 = 0;
            let mut h2: u64 = 0;
            let mut pow1: u64 = 1;
            let mut pow2: u64 = 1;

            for i in 0..len {
                let v = nums[i] as u64 + 1;
                h1 = (h1 * BASE1 + v) % MOD1;
                h2 = (h2 * BASE2 + v) % MOD2;
                if i + 1 < len {
                    pow1 = (pow1 * BASE1) % MOD1;
                    pow2 = (pow2 * BASE2) % MOD2;
                }
            }

            let mut counts: HashMap<(u64, u64), usize> = HashMap::with_capacity(n - len + 1);
            *counts.entry((h1, h2)).or_insert(0) += 1;

            for i in len..n {
                let out_v = nums[i - len] as u64 + 1;
                let in_v = nums[i] as u64 + 1;

                h1 = (h1 + MOD1 - (out_v * pow1) % MOD1) % MOD1;
                h1 = (h1 * BASE1 + in_v) % MOD1;

                h2 = (h2 + MOD2 - (out_v * pow2) % MOD2) % MOD2;
                h2 = (h2 * BASE2 + in_v) % MOD2;

                *counts.entry((h1, h2)).or_insert(0) += 1;
            }

            counts.values().any(|&c| c == 1)
        };

        let mut left = 1;
        let mut right = n;
        let mut ans = n;

        while left <= right {
            let mid = left + (right - left) / 2;
            if has_unique(mid) {
                ans = mid;
                right = mid - 1;
            } else {
                left = mid + 1;
            }
        }

        ans as i32
    }
}

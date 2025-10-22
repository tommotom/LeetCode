impl Solution {
    pub fn max_frequency(nums: Vec<i32>, k: i32, num_operations: i32) -> i32 {
        const MAXN: usize = 200_005;
        let mut freq = vec![0; MAXN];
        let mut prefix_sum = vec![0; MAXN];

        let max_value = *nums.iter().max().unwrap();
        let limit = (max_value + k + 2) as usize;

        for &num in &nums {
            freq[num as usize] += 1;
        }

        if num_operations == 0 {
            return *freq[..limit].iter().max().unwrap() as i32;
        } else {
            prefix_sum[0] = freq[0];
            for i in 1..limit {
                prefix_sum[i] = prefix_sum[i - 1] + freq[i];
            }

            let mut best = 0;

            for target in 0..=max_value as usize {
                let left = if target > k as usize { target - k as usize } else { 0 };
                let right = if (target + k as usize) < limit { target + k as usize } else { limit - 1 };

                let total = prefix_sum[right] - if left > 0 { prefix_sum[left - 1] } else { 0 };
                let changeable = (total - freq[target]) as i32;

                let possible = freq[target] as i32 + std::cmp::min(num_operations, changeable);
                best = std::cmp::max(best, possible);
            }

            return best;
        }
    }
}
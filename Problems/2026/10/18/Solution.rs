impl Solution {
    pub fn num_of_ways(nums: Vec<i32>) -> i32 {
        const MOD: u64 = 1_000_000_007;
        let n = nums.len();

        let mut c = vec![vec![0u64; n + 1]; n + 1];
        for i in 0..=n {
            c[i][0] = 1;
            for j in 1..=i {
                c[i][j] = (c[i - 1][j - 1] + c[i - 1][j]) % MOD;
            }
        }

        fn f(nums: &[i32], c: &Vec<Vec<u64>>) -> u64 {
            if nums.len() <= 2 {
                return 1;
            }
            let root = nums[0];
            let left: Vec<i32> = nums.iter().copied().filter(|&v| v < root).collect();
            let right: Vec<i32> = nums.iter().copied().filter(|&v| v > root).collect();

            c[left.len() + right.len()][right.len()] * f(&left, c) % MOD * f(&right, c) % MOD
        }

        ((f(&nums, &c) + MOD - 1) % MOD) as i32
    }
}

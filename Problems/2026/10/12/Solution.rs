impl Solution {
    pub fn max_sum(nums: Vec<i32>, k: i32) -> i32 {
        const MOD: i64 = 1_000_000_007;
        let mut cnt = vec![0i32; 30];

        for &num in nums.iter() {
            for i in 0..30 {
                if num & (1 << i) != 0 {
                    cnt[i] += 1;
                }
            }
        }

        let mut res: i64 = 0;
        for _ in 0..k {
            let mut cur: i64 = 0;
            for j in (0..30).rev() {
                if cnt[j] > 0 {
                    cur |= 1i64 << j;
                    cnt[j] -= 1;
                }
            }
            res = (res + cur * cur) % MOD;
        }

        res as i32
    }
}

impl Solution {
    pub fn xor_after_queries(nums: Vec<i32>, queries: Vec<Vec<i32>>) -> i32 {
        let mut nums: Vec<i64> = nums.into_iter().map(|num| num as i64).collect();
        let MOD = 1000000007 as i64;
        for q in queries {
            let (l, r, k, v) = (q[0], q[1], q[2], q[3]);
            let mut i = l as usize;
            while i <= r as usize {
                nums[i] = (nums[i] * v as i64) % MOD;
                i += k as usize;
            }
        }
        nums.into_iter().reduce(|a, b| a ^ b).unwrap() as i32
    }
}

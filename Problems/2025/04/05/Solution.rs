impl Solution {
    pub fn subset_xor_sum(nums: Vec<i32>) -> i32 {
        let n = nums.len();
        let mut ans = 0;
        for bit in 0..(2_i32.pow(n as u32)) {
            let mut total = 0;
            for i in 0..n {
                if ((1 << i) & bit) > 0 {
                    total ^= nums[i];
                }
            }
            ans += total;
        }
        ans
    }
}

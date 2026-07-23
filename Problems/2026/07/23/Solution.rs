impl Solution {
    pub fn unique_xor_triplets(nums: Vec<i32>) -> i32 {
        let mut n = nums.len();
        if n < 3 {
            return n as i32;
        }
        let mut ans = 0;
        while n > 0 {
            ans += 1;
            n /= 2;
        }
        2_i32.pow(ans)
    }
}

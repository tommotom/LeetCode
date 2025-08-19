impl Solution {
    pub fn zero_filled_subarray(nums: Vec<i32>) -> i64 {
        let mut contiguous = 0;
        let mut ans = 0;
        for num in nums {
            if num == 0 {
                contiguous += 1;
            } else {
                contiguous = 0;
            }
            ans += contiguous;
        }
        ans
    }
}

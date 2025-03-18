impl Solution {
    pub fn longest_nice_subarray(nums: Vec<i32>) -> i32 {
        let mut cur = 0;
        let mut l = -1;
        let mut ans = 0;
        for r in 0..nums.len() {
            while (cur & nums[r]) > 0 {
                l += 1;
                cur ^= nums[l as usize];
            }
            cur |= nums[r];
            ans = ans.max(r as i32 - l);
        }
        ans
    }
}

impl Solution {
    pub fn max_alternating_sum(mut nums: Vec<i32>) -> i64 {
        nums.sort_by(|a, b| a.abs().cmp(&b.abs()));
        println!("{:?}", nums);
        let (mut l, mut r) = (0, nums.len() - 1);
        let mut ans = 0_i64;
        let mut d = 0;
        while l <= r {
            if d == 0 {
                ans += (nums[r] * nums[r]) as i64;
                if r > 0 {
                    r -= 1;
                } else {
                    break;
                }
            } else {
                ans -= (nums[l] * nums[l]) as i64;
                l += 1;
            }
            d ^= 1;
        }
        ans
    }
}

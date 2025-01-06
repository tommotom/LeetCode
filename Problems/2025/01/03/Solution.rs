impl Solution {
    pub fn ways_to_split_array(nums: Vec<i32>) -> i32 {
        let mut right: i64 = 0;
        for num in &nums {
            right += *num as i64;
        }
        let mut left: i64 = 0;
        let mut ans = 0;
        for i in 0..(nums.len()-1) {
            left += nums[i] as i64;
            right -= nums[i] as i64;
            if left >= right {
                ans += 1;
            }
        }
        ans
    }
}

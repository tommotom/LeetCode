impl Solution {
    pub fn count_subarrays(nums: Vec<i32>) -> i32 {
        let mut ans = 0;
        for i in 0..(nums.len()-2) {
            if nums[i+1] % 2 == 0 && (nums[i] + nums[i+2]) == nums[i+1] / 2 {
                ans += 1;
            }
        }
        ans
    }
}

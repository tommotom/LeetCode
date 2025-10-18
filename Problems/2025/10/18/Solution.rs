impl Solution {
    pub fn max_distinct_elements(mut nums: Vec<i32>, k: i32) -> i32 {
        nums.sort();
        nums[0] -= k;
        let mut ans = 1;
        for i in 1..nums.len() {
            if nums[i-1] + 1 <= nums[i] + k {
                nums[i] = (nums[i-1] + 1).max(nums[i] - k);
                ans += 1;
            } else {
                nums[i] = nums[i-1];
            }
        }
        ans
    }
}

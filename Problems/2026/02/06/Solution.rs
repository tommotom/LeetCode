impl Solution {
    pub fn min_removal(mut nums: Vec<i32>, k: i32) -> i32 {
        nums.sort();
        let nums: Vec<i64> = nums.iter().map(|&num| num as i64).collect();
        let k = k as i64;
        let mut ans = nums.len() - 1;
        let mut r = 0;
        for l in 0..nums.len() {
            while r + 1 < nums.len() && nums[r] <= nums[l] * k {
                r += 1;
            }
            if nums[r] <= nums[l] * k {
                ans = ans.min(nums.len() - (r + 1 - l));
            } else {
                ans = ans.min(nums.len() - (r - l));
            }
        }
        ans as i32
    }
}

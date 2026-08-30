impl Solution {
    pub fn minimum_deletions(nums: Vec<i32>) -> i32 {
        let (mut min_i, mut max_i) = (0, 0);
        let (mut min, mut max) = (nums[0], nums[0]);
        for i in 1..nums.len() {
            if nums[i] < min {
                min_i = i;
                min = nums[i];
            }
            if nums[i] > max {
                max_i = i;
                max = nums[i];
            }
        }
        let l = min_i.min(max_i);
        let r = max_i.max(min_i);
        let n = nums.len();
        (r + 1).min(n - l).min(l + 1 + n - r) as i32
    }
}

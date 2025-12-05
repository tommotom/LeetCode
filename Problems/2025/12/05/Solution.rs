impl Solution {
    pub fn count_partitions(nums: Vec<i32>) -> i32 {
        let (mut l, mut ans) = (0, 0);
        let mut r: i32 = nums.iter().sum();
        for i in 0..(nums.len()-1) {
            l += nums[i];
            r -= nums[i];
            if (l - r) % 2 == 0 {
                ans += 1;
            }
        }
        ans
    }
}

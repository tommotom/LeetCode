impl Solution {
    pub fn left_right_difference(nums: Vec<i32>) -> Vec<i32> {
        let n = nums.len();
        let mut left_sum = Vec::new();
        let mut right_sum = Vec::new();
        let (mut l, mut r) = (0, 0);
        for i in 0..nums.len() {
            left_sum.push(l);
            l += nums[i];
            right_sum.push(r);
            r += nums[n-i-1];
        }
        let right_sum: Vec<i32> = right_sum.into_iter().rev().collect();
        let mut ans = Vec::new();
        for i in 0..nums.len() {
            ans.push((left_sum[i] - right_sum[i]).abs());
        }
        ans
    }
}

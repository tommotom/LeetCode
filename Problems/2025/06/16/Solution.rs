impl Solution {
    pub fn maximum_difference(nums: Vec<i32>) -> i32 {
        let mut min = nums[0];
        let mut ans = 0;
        for j in 1..nums.len() {
            ans = ans.max(nums[j] - min);
            min = min.min(nums[j]);
        }
        if ans == 0 { -1 } else { ans }
    }
}

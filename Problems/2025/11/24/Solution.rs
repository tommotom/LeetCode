impl Solution {
    pub fn prefixes_div_by5(nums: Vec<i32>) -> Vec<bool> {
        let mut ans = Vec::new();
        let mut sum = 0;
        for i in 0..nums.len() {
            sum *= 2;
            sum += nums[i];
            sum %= 5;
            ans.push(if sum == 0 {true} else {false});
        }
        ans
    }
}

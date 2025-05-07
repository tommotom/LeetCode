impl Solution {
    pub fn build_array(nums: Vec<i32>) -> Vec<i32> {
        let mut ans = vec![0; nums.len()];
        for (i, num) in nums.iter().enumerate() {
            ans[i] = nums[*num as usize];
        }
        ans
    }
}

impl Solution {
    pub fn max_increasing_subarrays(nums: Vec<i32>) -> i32 {
        let mut len = vec![1; nums.len()];
        for i in 1..nums.len() {
            if nums[i-1] < nums[i] {
                len[i] += len[i-1];
            }
        }
        let mut ans = 0;
        for i in 0..nums.len() {
            ans = ans.max(len[i] / 2);
            let l = len[i] as usize;
            if i >= l && len[i - l] >= len[i] {
                ans = ans.max(len[i]);
            }
        }
        ans
    }
}

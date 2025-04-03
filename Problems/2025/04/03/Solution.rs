impl Solution {
    pub fn maximum_triplet_value(nums: Vec<i32>) -> i64 {
        let n = nums.len();
        let mut left_max = vec![0; n];
        for i in 1..n {
            left_max[i] = left_max[i-1].max(nums[i-1] as i64);
        }
        let mut right_max = vec![0; n];
        for i in (0..n-1).rev() {
            right_max[i] = right_max[i+1].max(nums[i+1] as i64);
        }
        let mut ans = 0;
        for j in 1..n-1 {
            let diff = left_max[j] - nums[j] as i64;
            ans = ans.max(diff * right_max[j]);
        }
        ans
    }
}

impl Solution {
    pub fn maximum_triplet_value(nums: Vec<i32>) -> i64 {
        let n = nums.len();
        let mut right_max = vec![0; n];
        for i in (0..n-1).rev() {
            right_max[i] = right_max[i+1].max(nums[i+1] as i64);
        }
        let mut ans = 0;
        for i in 0..n-2 {
            for j in i+1..n-1 {
                let diff = (nums[i] - nums[j]) as i64;
                ans = ans.max(diff * right_max[j]);
            }
        }
        ans
    }
}

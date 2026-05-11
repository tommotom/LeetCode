impl Solution {
    pub fn maximum_jumps(nums: Vec<i32>, target: i32) -> i32 {
        let n = nums.len();
        let mut score = vec![-1; n];
        score[0] = 0;
        for i in 1..n {
            for j in 0..i {
                if score[j] == -1 {
                    continue;
                }
                if (nums[i] - nums[j]).abs() <= target {
                    score[i] = score[i].max(score[j] + 1);
                }
            }
        }
        score[n-1]
    }
}

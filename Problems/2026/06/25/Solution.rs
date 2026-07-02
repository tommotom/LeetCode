impl Solution {
    pub fn count_majority_subarrays(nums: Vec<i32>, target: i32) -> i32 {
        let n = nums.len();
        let mut c = vec![0; n+1];
        for i in 0..n {
            c[i+1] = c[i];
            if nums[i] == target {
                c[i+1] += 1;
            }
        }
        let mut ans = 0;
        for r in 0..n {
            for l in 0..=r {
                if c[r+1] - c[l] > (r - l + 1) / 2 {
                    ans += 1;
                }
            }
        }
        ans
    }
}

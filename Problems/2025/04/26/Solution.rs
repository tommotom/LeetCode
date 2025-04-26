impl Solution {
    pub fn count_subarrays(nums: Vec<i32>, min_k: i32, max_k: i32) -> i64 {
        let mut bad = -1;
        let mut min = -1;
        let mut max = -1;
        let mut ans = 0;
        for i in 0..nums.len() {
            if nums[i] < min_k || max_k < nums[i] {
                bad = i as i32;
            }
            if nums[i] == min_k {
                min = i as i32;
            }
            if nums[i] == max_k {
                max = i as i32;
            }
            ans += 0.max(min.min(max) - bad) as i64;
        }
        ans
    }
}

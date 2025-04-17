impl Solution {
    pub fn count_pairs(nums: Vec<i32>, k: i32) -> i32 {
        let n = nums.len();
        let mut ans = 0;
        for i in 0..(nums.len()-1) {
            for j in (i+1)..nums.len() {
                if nums[i] == nums[j] && (i as i32 * j as i32) % k == 0 {
                    ans += 1;
                }
            }
        }
        ans
    }
}

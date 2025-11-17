impl Solution {
    pub fn k_length_apart(nums: Vec<i32>, k: i32) -> bool {
        let k = k as usize;
        let mut seen = usize::MAX;
        for i in 0..nums.len() {
            if nums[i] == 1 {
                if seen != usize::MAX && i - seen <= k {
                    return false;
                }
                seen = i;
            }
        }
        true
    }
}

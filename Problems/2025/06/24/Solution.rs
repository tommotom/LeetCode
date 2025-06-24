impl Solution {
    pub fn find_k_distant_indices(nums: Vec<i32>, key: i32, k: i32) -> Vec<i32> {
        let k = k as usize;
        let mut ans = Vec::new();
        for i in 0..nums.len() {
            for diff in 0..(k+1) {
                if (i - diff < nums.len() && nums[i-diff] == key) || (i + diff < nums.len() && nums[i+diff] == key) {
                    ans.push(i as i32);
                    break;
                }
            }
        }
        ans
    }
}

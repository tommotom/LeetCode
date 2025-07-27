impl Solution {
    pub fn count_hill_valley(nums: Vec<i32>) -> i32 {
        let mut compressed = Vec::new();
        for i in 0..nums.len() {
            if i > 0 && nums[i-1] == nums[i] {
                continue;
            }
            compressed.push(nums[i]);
        }

        let mut ans = 0;
        for i in 2..compressed.len() {
            if compressed[i-2] < compressed[i-1] && compressed[i-1] > compressed[i] {
                ans += 1;
            } else if compressed[i-2] > compressed[i-1] && compressed[i-1] < compressed[i] {
                ans += 1;
            }
        }
        ans
    }
}

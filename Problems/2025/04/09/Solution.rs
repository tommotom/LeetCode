impl Solution {
    pub fn min_operations(mut nums: Vec<i32>, k: i32) -> i32 {
        nums.sort_by(|a, b| b.cmp(&a));
        if k > nums[nums.len()-1] {
            return -1;
        }
        let mut ans = 0;
        for i in 0..nums.len()-1 {
            if nums[i] != nums[i+1] {
                ans += 1;
            }
        }
        if k == nums[nums.len() -1] { ans } else { ans + 1 }
    }
}

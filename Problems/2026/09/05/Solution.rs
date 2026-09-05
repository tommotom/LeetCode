impl Solution {
    pub fn first_stable_index(nums: Vec<i32>, k: i32) -> i32 {
        let n = nums.len();
        let mut smallest = Vec::new();
        let mut min = i32::MAX;
        for i in (0..n).rev() {
            min = min.min(nums[i]);
            smallest.push(min);
        }
        smallest = smallest.into_iter().rev().collect();
        let mut max = i32::MIN;
        for i in 0..n {
            max = max.max(nums[i]);
            if max - smallest[i] <= k {
                return i as i32;
            }
        }
        -1
    }
}

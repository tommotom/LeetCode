impl Solution {
    pub fn min_moves(nums: Vec<i32>) -> i32 {
        let m = nums.iter().max().unwrap();
        nums.iter().map(|n| m - n).sum()
    }
}

impl Solution {
    pub fn min_moves(mut nums: Vec<i32>) -> i32 {
        nums.sort();
        let mut ans = 0;
        for i in 1..nums.len() {
            ans += nums[i] - nums[0];
        }
        ans
    }
}

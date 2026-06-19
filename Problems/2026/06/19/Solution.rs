impl Solution {
    pub fn largest_altitude(gain: Vec<i32>) -> i32 {
        let mut ans = 0;
        let mut cur = 0;
        for g in gain {
            cur += g;
            ans = ans.max(cur);
        }
        ans
    }
}

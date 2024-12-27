use std::cmp;

impl Solution {
    pub fn max_score_sightseeing_pair(values: Vec<i32>) -> i32 {
        let mut best = values[0];
        let mut ans = 0;
        for i in 1..values.len() {
            ans = cmp::max(ans, best + values[i] - i as i32);
            best = cmp::max(best, values[i] + i as i32);
        }
        ans
    }
}

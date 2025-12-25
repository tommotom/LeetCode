impl Solution {
    pub fn maximum_happiness_sum(mut happiness: Vec<i32>, k: i32) -> i64 {
        happiness.sort_by(|a, b| b.cmp(&a));
        let mut ans = 0;
        let mut turn = 0;
        for i in 0..(k as usize) {
            ans += ((happiness[i] - turn) as i64).max(0);
            turn += 1;
        }
        ans
    }
}

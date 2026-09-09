impl Solution {
    pub fn count_commas(n: i64) -> i64 {
        let mut p = 1000_i64;
        let mut ans = 0_i64;
        while p <= n {
            ans += n - p + 1;
            p *= 1000;
        }
        ans
    }
}

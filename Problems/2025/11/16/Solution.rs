impl Solution {
    pub fn num_sub(s: String) -> i32 {
        let mut ans = 0;
        let mut count = 0;
        let m = 1000000007;
        for c in s.chars() {
            if c == '0' {
                count = 0;
            } else {
                count += 1;
            }
            ans += count;
            ans %= m
        }
        ans
    }
}

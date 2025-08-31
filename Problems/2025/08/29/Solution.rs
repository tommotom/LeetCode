impl Solution {
    pub fn flower_game(n: i32, m: i32) -> i64 {
        let mut ans = 0;
        for x in 1..(n+1) {
            if m % 2 == 0 {
                ans += (m / 2) as i64
            } else {
                ans += ((m - 1)/2 + ((x + m) % 2)) as i64
            }
        }
        ans
    }
}
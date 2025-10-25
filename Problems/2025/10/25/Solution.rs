impl Solution {
    pub fn total_money(n: i32) -> i32 {
        if n == 0 {
            return 0;
        }
        Self::total_money(n-1) + ((n-1) / 7) + (n-1) % 7 + 1
    }
}

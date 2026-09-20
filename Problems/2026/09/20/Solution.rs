impl Solution {
    pub fn reverse_degree(s: String) -> i32 {
        let mut ans = 0;
        for (i, c) in s.chars().enumerate() {
            let rev = 'z'.to_ascii_lowercase() as u8 - c.to_ascii_lowercase() as u8 + 1;
            ans += rev as i32 * (i as i32 + 1);
        }
        ans
    }
}

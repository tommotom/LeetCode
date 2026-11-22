impl Solution {
    pub fn check_string(s: String) -> bool {
        let mut seen = false;
        for c in s.chars() {
            if c == 'a' && seen {
                return false;
            }
            if c == 'b' {
                seen = true;
            }
        }
        true
    }
}

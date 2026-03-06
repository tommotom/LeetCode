impl Solution {
    pub fn check_ones_segment(s: String) -> bool {
        let s: Vec<char> = s.chars().collect();
        let mut seen_zero = false;
        for c in s {
            if c == '0' {
                seen_zero = true;
            } else if seen_zero {
                return false;
            }
        }
        true
    }
}

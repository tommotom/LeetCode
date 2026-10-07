impl Solution {
    pub fn min_add_to_make_valid(s: String) -> i32 {
        let mut left = 0;
        let mut d = 0;
        for c in s.chars() {
            if c == '(' {
                d += 1;
            } else {
                d -= 1;
            }
            if d < 0 {
                d = 0;
                left += 1;
            }
        }
        let mut right = 0;
        d = 0;
        for c in s.chars().rev() {
            if c == ')' {
                d += 1;
            } else {
                d -= 1;
            }
            if d < 0 {
                d = 0;
                right += 1;
            }
        }
        left + right
    }
}

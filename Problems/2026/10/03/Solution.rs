impl Solution {
    pub fn check_valid_string(s: String) -> bool {
        let mut d = 0;
        let mut x = 0;
        for c in s.chars() {
            if c == '(' {
                d += 1;
            } else if c == ')' {
                d -= 1;
            } else {
                x += 1;
            }
            if d < 0 {
                if x > 0 {
                    d += 1;
                    x -= 1;
                } else {
                    return false;
                }
            }
        }
        d = 0;
        x = 0;
        for c in s.chars().rev() {
            if c == ')' {
                d += 1;
            } else if c == '(' {
                d -= 1;
            } else {
                x += 1;
            }
            if d < 0 {
                if x > 0 {
                    d += 1;
                    x -= 1;
                } else {
                    return false;
                }
            }
        }
        true
    }
}

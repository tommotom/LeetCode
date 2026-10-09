impl Solution {
    pub fn min_insertions(s: String) -> i32 {
        let mut vec = Vec::new();
        let mut r = 0;
        let mut ans = 0;
        for c in s.chars() {
            if c == '(' {
                if r % 2 == 1 {
                    ans += 1;
                    vec.push(')');
                }
                r = 0;
                vec.push('(')
            } else {
                r += 1;
                if r == 2 {
                    vec.push(')');
                    r = 0;
                }
            }
        }
        if r == 1 {
            ans += 1;
            vec.push(')');
        }

        let mut d = 0;
        for c in vec.iter() {
            if *c == '(' {
                d += 1;
            } else {
                d -= 1;
            }
            if d < 0 {
                d = 0;
                ans += 1;
            }
        }

        d = 0;
        for c in vec.iter().rev() {
            if *c == ')' {
                d += 1;
            } else {
                d -= 1;
            }
            if d < 0 {
                d = 0;
                ans += 2;
            }
        }

        ans
    }
}

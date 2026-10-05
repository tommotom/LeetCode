impl Solution {
    pub fn score_of_parentheses(s: String) -> i32 {
        if s == "()".to_string() {
            return 1;
        }
        if s == "" {
            return 0;
        }
        let mut st = Vec::new();
        let mut d = 0;
        let mut ans = 0;
        for c in s.chars() {
            if c == '(' {
                d += 1;
            } else {
                d -= 1;
            }
            if d == 0 {
                if st.len() > 1 {
                    ans += Self::score_of_parentheses(st.iter().skip(1).collect()) * 2;
                } else {
                    ans += 1;
                }
                st = Vec::new();
            } else {
                st.push(c);
            }
        }
        ans
    }
}

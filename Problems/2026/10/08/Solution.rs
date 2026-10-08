impl Solution {
    pub fn remove_outer_parentheses(s: String) -> String {
        let mut d = 0;
        let mut ans = Vec::new();
        for c in s.chars() {
            if c == '(' {
                if d > 0 {
                    ans.push(c);
                }
                d += 1;
            } else {
                d -= 1;
                if d > 0 {
                    ans.push(c);
                }
            }
        }
        ans.iter().collect()
    }
}

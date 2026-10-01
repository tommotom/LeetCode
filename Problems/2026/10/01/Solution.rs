impl Solution {
    pub fn is_valid(s: String) -> bool {
        let mut st = Vec::new();
        for c in s.chars() {
            if c == ')' && (st.len() == 0 || st.pop().unwrap() != '(') {
                return false;
            } else if c == '}' && (st.len() == 0 || st.pop().unwrap() != '{') {
                return false;
            } else if c == ']' && (st.len() == 0 || st.pop().unwrap() != '[') {
                return false;
            } else if c == '(' || c == '{' || c == '[' {
                st.push(c);
            }
        }
        st.len() == 0
    }
}

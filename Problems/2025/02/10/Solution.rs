impl Solution {
    pub fn clear_digits(s: String) -> String {
        let mut st = Vec::new();
        for c in s.chars() {
            if c.is_ascii_digit() {
                st.pop();
            } else {
                st.push(c);
            }

        }
        st.into_iter().collect::<String>()
    }
}

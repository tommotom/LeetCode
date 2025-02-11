impl Solution {
    pub fn remove_occurrences(s: String, part: String) -> String {
        let mut st = Vec::new();
        let part_vec: Vec<char> = part.chars().collect();
        for c in s.chars() {
            st.push(c);
            if st.len() >= part.len() && Self::has_part(&st, &part_vec) {
                for i in 0..part.len() {
                    st.pop();
                }
            }
        }
        st.iter().collect()
    }

    fn has_part(st: &Vec<char>, part_vec: &Vec<char>) -> bool {
        let base = st.len() - part_vec.len();
        for i in 0..part_vec.len() {
            if part_vec[i] != st[base + i] {
                return false;
            }
        }
        true
    }
}

impl Solution {
    pub fn are_almost_equal(s1: String, s2: String) -> bool {
        let s1_char: Vec<char> = s1.chars().collect();
        let s2_char: Vec<char> = s2.chars().collect();
        let mut diffs = 0;
        let mut last = 0;
        for i in 0..s1_char.len() {
            if s1_char[i] != s2_char[i] {
                if diffs == 2 {
                    return false;
                } else if diffs == 1 && (s1_char[last] != s2_char[i] || s1_char[i] != s2_char[last]) {
                    return false;
                }
                last = i;
                diffs += 1;

            }
        }
        diffs != 1
    }
}

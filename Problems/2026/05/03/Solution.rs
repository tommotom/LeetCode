impl Solution {
    pub fn rotate_string(s: String, goal: String) -> bool {
        if s.len() != goal.len() {
            return false;
        }
        let s: Vec<char> = s.chars().collect();
        let goal: Vec<char> = goal.chars().collect();
        let n = s.len();
        for i in 0..n {
            let mut is_valid = true;
            let mut s_i = i;
            for j in 0..n {
                if s[s_i] != goal[j] {
                    is_valid = false;
                    break;
                }
                s_i = (s_i + 1) % n;
            }
            if is_valid {
                return true;
            }
        }
        false
    }
}

impl Solution {
    pub fn min_changes(s: String) -> i32 {
        let mut ans = 0;
        let s: Vec<char> = s.chars().collect();
        for i in (0..s.len()).step_by(2) {
            if s[i] != s[i+1] {
                ans += 1;
            }
        }
        ans
    }
}

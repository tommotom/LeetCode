use std::collections::HashSet;

impl Solution {
    pub fn has_all_codes(s: String, k: i32) -> bool {
        if s.len() < k as usize {
            return false;
        }
        let mut sub = HashSet::new();
        let s: Vec<char> = s.chars().collect();
        let mut cur = 0;
        for i in 0..(k as usize - 1) {
            cur *= 2;
            if s[i] == '1' {
                cur += 1;
            }
        }
        for i in (k as usize - 1)..s.len() {
            cur *= 2;
            if s[i] == '1' {
                cur += 1;
            }
            sub.insert(cur);
            if s[i+1-(k as usize)] == '1' {
                cur -= i32::pow(2, k as u32 - 1);
            }
        }
        sub.len() as i32 == i32::pow(2, k as u32)
    }
}

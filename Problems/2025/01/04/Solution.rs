use std::collections::HashSet;

impl Solution {
    pub fn count_palindromic_subsequence(s: String) -> i32 {
        let mut left = [0; 26];
        let mut right = [0; 26];
        for c in s.chars() {
            let i = ((c.to_ascii_lowercase()) as i32 - 97) as usize;
            right[i] += 1;
        }
        let mut seen = HashSet::new();
        for c in s.chars() {
            let i = ((c.to_ascii_lowercase()) as i32 - 97) as usize;
            right[i] -= 1;
            for j in 0..26 {
                if left[j] > 0 && right[j] > 0 {
                    seen.insert(format!("{}{}", j, c));
                }
            }
            left[i] += 1;
        }
        return seen.len() as i32;
    }
}

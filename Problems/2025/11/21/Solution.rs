use std::collections::HashSet;

impl Solution {
    pub fn count_palindromic_subsequence(s: String) -> i32 {
        fn to_usize(c: char) -> usize {
            (c as u32 - 'a' as u32) as usize
        }
        let mut back = vec![0; 26];
        let mut forward = vec![0; 26];
        let s: Vec<usize> = s.chars().map(|c| to_usize(c)).collect();
        back[s[0]] += 1;
        for i in 1..s.len() {
            forward[s[i]] += 1;
        }
        let mut counter = HashSet::new();
        for i in 1..(s.len()-1) {
            forward[s[i]] -= 1;
            for j in 0..26 {
                if forward[j] > 0 && back[j] > 0 {
                    counter.insert((s[i], j));
                }
            }
            back[s[i]] += 1;
        }
        counter.len() as i32
    }
}

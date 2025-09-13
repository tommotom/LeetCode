use std::collections::HashMap;

impl Solution {
    pub fn max_freq_sum(s: String) -> i32 {
        fn is_vowel(c: char) -> bool {
            c == 'a' || c == 'i' || c == 'u' || c == 'e' || c == 'o'
        }

        let mut vowel = HashMap::new();
        let mut consonant = HashMap::new();
        for c in s.chars() {
            if is_vowel(c) {
                *vowel.entry(c).or_insert(0) += 1;
            } else {
                *consonant.entry(c).or_insert(0) += 1;
            }
        }

        vowel.into_values().max().unwrap_or_default() + consonant.into_values().max().unwrap_or_default()
    }
}

impl Solution {
    fn count(word: String) -> [i32; 26] {
        let mut counter = [0; 26];
        for c in word.chars() {
            counter[(c.to_ascii_lowercase() as u8 - 97) as usize] += 1;
        }
        counter
    }

    fn is_universal(word: String, max_count: [i32; 26]) -> bool {
        let counter = Self::count(word);
        for i in 0..26 {
            if counter[i] < max_count[i] {
                return false;
            }
        }
        true
    }

    pub fn word_subsets(words1: Vec<String>, words2: Vec<String>) -> Vec<String> {
        let words2_counters: Vec<[i32; 26]> = words2.into_iter().map(|word| Self::count(word)).collect();
        let mut max_count = [0; 26];
        for word2_counter in words2_counters {
            for i in 0..26 {
                max_count[i] = max_count[i].max(word2_counter[i]);
            }
        }
        return words1.into_iter().filter(|word| Self::is_universal(word.to_string(), max_count.clone())).collect();
    }
}

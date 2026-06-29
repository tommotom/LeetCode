impl Solution {
    pub fn num_of_strings(patterns: Vec<String>, word: String) -> i32 {
        fn is_substr(pattern: &Vec<char>, word: &Vec<char>) -> bool {
            for i in 0..word.len() {
                let mut is_valid = true;
                for j in 0..pattern.len() {
                    if i + j == word.len() || pattern[j] != word[i+j] {
                        is_valid = false;
                        break;
                    }
                }
                if is_valid {
                    return true;
                }
            }
            false
        }
        let word_vec: Vec<char> = word.chars().collect();
        patterns.iter().map(|pattern| is_substr(&pattern.chars().collect(), &word_vec)).filter(|x| *x).count() as i32
    }
}

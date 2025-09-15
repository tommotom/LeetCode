use std::collections::HashSet;

impl Solution {
    pub fn can_be_typed_words(text: String, broken_letters: String) -> i32 {
        let broken_letters: HashSet<char> = broken_letters.chars().collect();
        fn isValid(word: String, broken_letters: &HashSet<char>) -> bool {
            for c in word.chars() {
                if broken_letters.contains(&c) {
                    return false;
                }
            }
            true
        }
        text.split(' ').filter(|word| isValid(word.to_string(), &broken_letters)).count() as i32
    }
}

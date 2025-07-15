impl Solution {
    pub fn is_valid(word: String) -> bool {
        if word.len() < 3 {
            return false;
        }
        let mut vowel = false;
        let mut consonant = false;
        for c in word.chars() {
            if !c.is_alphanumeric() {
                return false;
            }
            if c.is_digit(10) {
                continue;
            }
            let l = c.to_lowercase().next().unwrap();
            if l == 'a' || l == 'i' || l == 'u' || l == 'e' || l == 'o' {
                vowel = true;
            } else {
                consonant = true;
            }
        }
        vowel && consonant
    }
}

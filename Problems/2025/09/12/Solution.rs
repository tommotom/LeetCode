impl Solution {
    pub fn does_alice_win(s: String) -> bool {
        fn is_vowel(c: char) -> bool {
            c == 'a' || c == 'i' || c == 'u' || c == 'e' || c == 'o'
        }
        s.chars().filter(|c| is_vowel(*c)).count() > 0
    }
}

impl Solution {
    pub fn sort_vowels(s: String) -> String {
        fn is_vowel(c: char) -> bool {
            c == 'a' || c == 'i' || c == 'u' || c == 'e' || c == 'o' || c == 'A' || c == 'I' || c == 'U' || c == 'E' || c == 'O'
        }
        let mut vowels: Vec<char> = s.chars().filter(|c| is_vowel(*c)).collect();
        vowels.sort();
        let mut i = 0;
        let mut ans = Vec::new();
        for c in s.chars() {
            if is_vowel(c) {
                ans.push(vowels[i]);
                i += 1;
            } else {
                ans.push(c);
            }
        }
        ans.iter().collect::<String>()
    }
}

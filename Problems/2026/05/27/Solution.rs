
impl Solution {
    pub fn number_of_special_chars(word: String) -> i32 {
        let mut seen_at = vec![usize::MAX; 26];
        let word: Vec<char> = word.chars().collect();
        for i in 0..word.len() {
            if word[i].is_lowercase() {
                let j = word[i].to_ascii_lowercase() as u8 as usize - 97;
                seen_at[j] = i;
            }
        }
        let mut seen = vec![false; 26];
        let mut ans = 0;
        for i in 0..word.len() {
            if word[i].is_uppercase() {
                let j = word[i].to_ascii_lowercase() as u8 as usize - 97;
                if seen[j] {
                    continue;
                }
                seen[j] = true;
                if seen_at[j] < i {
                    ans += 1;
                }
            }
        }
        ans
    }
}

impl Solution {
    fn has_prefix(word: String, pref: String) -> bool {
        if (word.len() < pref.len()) {
            return false;
        }
        for (i, c) in pref.chars().enumerate() {
            if word.chars().nth(i).unwrap() != c {
                return false;
            }
        }
        true
    }

    pub fn prefix_count(words: Vec<String>, pref: String) -> i32 {
        let mut ans = 0;
        for word in words {
            if Self::has_prefix(word, pref.clone()) {
                ans += 1;
            }
        }
        ans
    }
}

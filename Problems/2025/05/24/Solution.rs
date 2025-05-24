impl Solution {
    pub fn find_words_containing(words: Vec<String>, x: char) -> Vec<i32> {
        let mut ans = Vec::new();
        for i in 0..words.len() {
            let mut found = false;
            for c in words[i].chars() {
                if c == x {
                    found = true;
                    break;
                }
            }
            if found {
                ans.push(i as i32);
            }
        }
        ans
    }
}

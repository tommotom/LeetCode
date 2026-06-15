impl Solution {
    pub fn map_word_weights(words: Vec<String>, weights: Vec<i32>) -> String {
        let mut a = 'a'.to_ascii_lowercase() as u8;
        let mut arr = Vec::new();
        for word in words {
            let mut sum = 0;
            for c in word.chars() {
                sum += weights[c.to_ascii_lowercase() as usize - a as usize];
                sum %= 26;
            }
            arr.push(((25 - sum) as u8  + a)as char);
        }
        arr.iter().collect()
    }
}

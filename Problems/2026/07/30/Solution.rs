impl Solution {
    pub fn minimum_pushes(word: String) -> i32 {
        let mut counter = vec![0; 26];
        for c in word.chars() {
            counter[(c.to_ascii_lowercase() as u8 - b'a') as usize] += 1;
        }
        counter.sort_by(|a, b| b.cmp(&a));
        let mut ans = 0;
        for i in 0..26 {
            ans += counter[i] * (i / 8 + 1)
        }
        ans as i32
    }
}

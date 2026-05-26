impl Solution {
    pub fn number_of_special_chars(word: String) -> i32 {
        let mut lower = [false; 26];
        let mut upper = [false; 26];
        for c in word.bytes() {
            match c {
                b'a'..=b'z' => lower[(c - b'a') as usize] = true,
                b'A'..=b'Z' => upper[(c - b'A') as usize] = true,
                _ => {}
            }
        }
        (0..26).filter(|&i| lower[i] && upper[i]).count() as i32
    }
}

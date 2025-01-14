impl Solution {
    pub fn minimum_length(s: String) -> i32 {
        let mut counter = [0; 26];
        for c in s.chars() {
            let i = c.to_ascii_lowercase() as usize - 97;
            counter[i] += 1;
            if counter[i] == 3 {
                counter[i] = 1;
            }
        }
        return counter.iter().sum();
    }
}

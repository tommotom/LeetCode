impl Solution {
    pub fn max_difference(s: String) -> i32 {
        let mut counter = vec![0; 26];
        for c in s.chars() {
            let i = (c as u8 - 'a' as u8) as usize;
            counter[i] += 1;
        }
        let odd = *counter.iter().filter(|c| *c % 2 == 1).max().unwrap();
        let even = *counter.iter().filter(|c| **c > 0 && *c % 2 == 0).min().unwrap();
        odd - even
    }
}

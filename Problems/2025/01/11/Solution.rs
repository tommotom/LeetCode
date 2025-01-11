impl Solution {
    pub fn can_construct(s: String, k: i32) -> bool {
        if s.len() < k as usize {
            return false;
        }

        let mut counter = [0; 26];
        for c in s.chars() {
            let i = c.to_ascii_lowercase() as usize - 97;
            counter[i] += 1;
        }
        let mut odds = 0;
        for i in 0..26 {
            if counter[i] % 2 == 1 {
                odds += 1;
            }
        }
        return odds <= k;
    }
}

impl Solution {
    pub fn smallest_palindrome(s: String) -> String {
        fn to_i(c: char) -> usize {
            (c.to_ascii_lowercase() as u8 - b'a') as usize
        }
        let mut counter = vec![0; 26];
        for c in s.chars() {
            counter[to_i(c)] += 1;
        }
        let mut vec = Vec::new();
        for i in 0..26 {
            while counter[i] > 1 {
                vec.push((i as u8 + b'a') as char);
                counter[i] -= 2;
            }
        }

        let mut center = None;
        for i in 0..26 {
            if counter[i] == 1 {
                center = Some((i as u8 + b'a') as char);
                break;
            }
        }

        let mut ans: String = vec.iter().collect();
        if let Some(c) = center {
            ans.push(c);
        }
        ans.extend(vec.iter().rev());

        ans
    }
}

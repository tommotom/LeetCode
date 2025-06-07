impl Solution {
    pub fn robot_with_string(s: String) -> String {
        let a = b'a';
        let mut freq = vec![0; 26];
        let bytes = s.as_bytes();

        for &b in bytes {
            freq[(b - a) as usize] += 1;
        }

        let mut stack: Vec<u8> = Vec::new();
        let mut result = Vec::new();

        let mut has_smaller = |top: usize, freq: &Vec<usize>| -> bool {
            (0..top).any(|i| freq[i] > 0)
        };

        for &b in bytes {
            let ch = (b - a) as usize;
            freq[ch] -= 1;
            stack.push(b);
            while let Some(&last) = stack.last() {
                if has_smaller((last - a) as usize, &freq) {
                    break;
                }
                result.push(stack.pop().unwrap());
            }
        }

        String::from_utf8(result).unwrap()
    }
}

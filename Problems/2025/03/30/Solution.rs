use std::collections::HashSet;

impl Solution {
    pub fn partition_labels(s: String) -> Vec<i32> {
        fn to_i(c: char) -> usize {
            c.to_ascii_lowercase() as usize - 'a'.to_ascii_lowercase() as usize
        }

        let mut counter = vec![0; 26];
        for c in s.chars() {
            counter[to_i(c)] += 1;
        }

        let mut l = 0;
        let mut ans = Vec::new();
        let mut seen = HashSet::new();
        for c in s.chars() {
            counter[to_i(c)] -= 1;
            seen.insert(c);
            l += 1;
            let mut isValid = true;
            for s in &seen {
                if counter[to_i(*s)] > 0 {
                    isValid = false;
                    break;
                }
            }
            if isValid {
                ans.push(l);
                l = 0;
            }
        }
        ans
    }
}

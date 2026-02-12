use std::collections::HashSet;

impl Solution {
    pub fn longest_balanced(s: String) -> i32 {
        fn to_index(c: char) -> usize {
            (c.to_ascii_lowercase() as u8 - 'a'.to_ascii_lowercase() as u8) as usize
        }
        fn is_balanced(counter: &Vec<i32>) -> bool {
            counter.iter().filter(|&&x| x != 0).collect::<HashSet<_>>().len() <= 1
        }
        let chars: Vec<char> = s.chars().collect();
        let mut ans = 0;
        let mut counter = vec![0; 26];
        for i in 0..chars.len() {
            counter[to_index(chars[i])] += 1;
            let mut diff = counter.clone();
            for j in 0..=i {
                if is_balanced(&diff) {
                    ans = ans.max(i - j + 1);
                }
                diff[to_index(chars[j])] -= 1;
            }
        }
        ans as i32
    }
}

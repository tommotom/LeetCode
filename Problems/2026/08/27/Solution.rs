impl Solution {
    pub fn lex_greater_permutation(s: String, target: String) -> String {
        let mut cnt = vec![0i32; 26];
        for c in s.chars() {
            cnt[(c as u8 - b'a') as usize] += 1;
        }

        let mut res = String::new();
        let n = target.len();

        for (i, c) in target.chars().enumerate() {
            let target_char = (c as u8 - b'a') as usize;

            // Case 1: First try to place the same character as target[i] at the current position
            if cnt[target_char] > 0 {
                cnt[target_char] -= 1;
                // Check if the remaining characters can form a string greater than target[i+1:]
                if Self::can_form_greater(&cnt, &target[i+1..]) {
                    res.push(c);
                    continue;
                }
                // Cannot form a larger string, backtrack
                cnt[target_char] += 1;
            }

            // Case 2: Place a character greater than target[i] at the current position
            for j in (target_char + 1)..26 {
                if cnt[j] > 0 {
                    cnt[j] -= 1;
                    res.push((b'a' + j as u8) as char);
                    // Fill remaining positions with the smallest lexicographical order
                    res.push_str(&Self::get_min_string(&cnt));
                    return res;
                }
            }

            // No feasible solution found, return directly
            return String::new();
        }

        String::new()
    }

    // Check if the remaining characters can form a string greater than the suffix.
    fn can_form_greater(cnt: &[i32], suffix: &str) -> bool {
        let max_str = Self::get_max_string(cnt);
        max_str.as_str() > suffix
    }

    // Get the lexicographically smallest string (in ascending order)
    fn get_min_string(cnt: &[i32]) -> String {
        let total_len: usize = cnt.iter().map(|&c| c as usize).sum();
        let mut res = String::with_capacity(total_len);

        for i in 0..26 {
            res.push_str(&((b'a' + i as u8) as char).to_string().repeat(cnt[i] as usize));
        }
        res
    }

    // Get the maximum lexicographical string (in descending order)
    fn get_max_string(cnt: &[i32]) -> String {
        let total_len: usize = cnt.iter().map(|&c| c as usize).sum();
        let mut res = String::with_capacity(total_len);

        for i in (0..26).rev() {
            res.push_str(&((b'a' + i as u8) as char).to_string().repeat(cnt[i] as usize));
        }
        res
    }
}

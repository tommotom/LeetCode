impl Solution {
    pub fn max_operations(s: String) -> i32 {
        let s: Vec<char> = s.chars().collect();
        let mut i = 0;
        while i < s.len() && s[i] == '0' {
            i += 1;
        }
        if i == s.len() {
            return 0;
        }

        let mut j = i + 1;
        let mut count = 1;
        while j < s.len() && !(s[j-1] == '0' && s[j] == '1') {
            if s[j] == '1' {
                count += 1;
            }
            j += 1;
        }
        let mut ans = 0;
        while j < s.len() {
            ans += count;
            if s[j] == '1' {
                count += 1;
            }
            j += 1;
            while j < s.len() && !(s[j-1] == '0' && s[j] == '1') {
                if s[j] == '1' {
                    count += 1;
                }
                j += 1;
            }
        }
        if s[s.len()-1] == '0' {ans + count} else {ans}
    }
}

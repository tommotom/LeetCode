impl Solution {
    pub fn min_operations(s: String) -> i32 {
        let mut a = 0;
        let mut b = 0;
        let s: Vec<char> = s.chars().collect();
        for i in 0..s.len() {
            if i % 2 == 0 {
                if s[i] == '0' {
                    a += 1;
                } else {
                    b += 1;
                }
            } else {
                if s[i] == '0' {
                    b += 1;
                } else {
                    a += 1;
                }

            }
        }
        a.min(b)
    }
}

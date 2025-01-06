impl Solution {
    pub fn max_score(s: String) -> i32 {
        let mut ones = s.chars().filter(|c| *c == '1').count();
        let mut zeros = 0;
        let mut ans = 0;
        for c in s[0..s.len()-1].chars() {
            if c == '0' {
                zeros += 1;
            } else {
                ones -= 1;
            }
            ans = ans.max(ones + zeros);
        }
        ans as i32
    }
}

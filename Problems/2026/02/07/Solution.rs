impl Solution {
    pub fn minimum_deletions(s: String) -> i32 {
        let chars: Vec<char> = s.chars().collect();
        let mut a = chars.iter().filter(|&c| *c == 'a').count();
        let mut b = 0;
        let mut ans = a;
        for &c in &chars {
            if c == 'a' {
                a -= 1;
            } else {
                b += 1;
            }
            ans = ans.min(a + b);
        }
        ans as i32
    }
}

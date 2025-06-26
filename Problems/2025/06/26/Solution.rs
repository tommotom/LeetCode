impl Solution {
    pub fn longest_subsequence(s: String, k: i32) -> i32 {
        let s: Vec<i32> = s.chars().map(|c| c.to_digit(10).unwrap() as i32).collect();
        let mut ans = 0;
        for i in (0..s.len()).rev() {
            let mut num = s[i];
            let mut len = 1;
            for j in (0..i).rev() {
                if s[j] == 0 {
                    len += 1;
                    continue;
                }
                if len > 30 {
                    continue;
                }
                let next = num + 2_i32.pow(len);
                if 0 <= next && next <= k {
                    num = next;
                    len += 1;
                }
            }
            ans = ans.max(len);
        }
        ans as i32
    }
}

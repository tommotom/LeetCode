impl Solution {
    pub fn num_steps(s: String) -> i32 {
        let mut s: Vec<u32> = s.chars().map(|c| c.to_digit(10 as u32).unwrap()).rev().collect();
        let mut ans = 0;
        let mut carry = 0;
        let mut i = 0;
        while i < s.len() - 1 || s[i] == 0 || carry == 1 {
            let tmp = carry + s[i];
            carry = tmp / 2;
            s[i] = tmp % 2;
            if s[i] == 1 {
                carry += 1;
                ans += 1;
            }
            ans += 1;
            i += 1;
            if i == s.len() && carry > 0 {
                s.push(carry);
                carry = 0;
            }
        }

        ans
    }
}

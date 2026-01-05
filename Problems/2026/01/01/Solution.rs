impl Solution {
    pub fn plus_one(mut digits: Vec<i32>) -> Vec<i32> {
        let mut i = digits.len() - 1;
        let mut carry = 1;
        while i < digits.len() && carry > 0 {
            carry = (digits[i] + 1) / 10;
            digits[i] = (digits[i] + 1) % 10;
            i -= 1;
        }
        if carry > 0 {
            let mut ans = vec![1];
            ans.append(&mut digits);
            return ans;
        }
        digits
    }
}

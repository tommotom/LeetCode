impl Solution {
    pub fn maximum69_number (num: i32) -> i32 {
        let mut ans = 0;
        let mut changed = false;
        for c in num.to_string().chars() {
            ans *= 10;
            let d = c as i32 - 48;
            if !changed && d == 6 {
                changed = true;
                ans += 9;
            } else {
                ans += d;
            }
        }
        ans
    }
}

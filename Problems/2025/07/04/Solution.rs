impl Solution {
    pub fn kth_character(k: i64, operations: Vec<i32>) -> char {
        let mut ans = 0;
        let mut k = k;
        while k != 1 {
            let t = 63 - k.leading_zeros();
            let t = if (1 << t) == k { t - 1 } else { t };
            k -= 1 << t;
            if operations[t as usize] != 0 {
                ans += 1;
            }
        }
        (b'a' + (ans % 26) as u8) as char
    }
}

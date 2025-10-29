impl Solution {
    pub fn smallest_number(mut n: i32) -> i32 {
        let mut len = 0;
        while n > 0 {
            len += 1;
            n = n / 2;
        }
        (2_i32.pow(len)) - 1
    }
}

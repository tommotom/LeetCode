impl Solution {
    pub fn check_powers_of_three(mut n: i32) -> bool {
        while n > 0 {
            let mut x = 0;
            while 3_i32.pow(x) <= n {
                x += 1;
            }
            n -= 3_i32.pow(x-1);
            if 3_i32.pow(x-1) <= n {
                return false;
            }
        }
        true
    }
}

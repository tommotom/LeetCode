impl Solution {
    pub fn get_no_zero_integers(n: i32) -> Vec<i32> {
        fn is_no_zero_integer(mut n: i32) -> bool {
            while n > 0 {
                if n % 10 == 0 {
                    return false;
                }
                n /= 10;
            }
            true
        }
        for num in 1..n {
            if is_no_zero_integer(num) && is_no_zero_integer(n - num) {
                return vec![num, n - num];
            }
        }
        vec![0, n]
    }
}

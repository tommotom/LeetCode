impl Solution {
    pub fn smallest_number(n: i32, t: i32) -> i32 {
        fn digit_product(mut num: i32) -> i32 {
            let mut res = 1;
            while num > 0 {
                res *= num % 10;
                num /= 10;
            }
            res
        }
        let mut num = n;
        while true {
            if digit_product(num) % t == 0 {
                return num;
            }
            num += 1;
        }
        0
    }
}

impl Solution {
    pub fn count_prime_set_bits(left: i32, right: i32) -> i32 {
        fn number_of_bits(mut num: i32) -> i32 {
            let mut ret = 0;
            while num > 0 {
                ret += num % 2;
                num /= 2;
            }
            ret
        }

        fn is_prime(mut num: i32) -> bool {
            if num < 2 {
                return false;
            }
            let mut d = 2;
            let mut count = 0;
            while d * d <= num {
                while num % d == 0 {
                    count += 1;
                    num /= d;
                }
                d += 1;
            }
            count == 0
        }

        let mut ans = 0;
        for num in left..=right {
            let b = number_of_bits(num);
            if is_prime(b) {
                ans += 1;
            }
        }
        ans
    }
}

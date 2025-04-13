impl Solution {
    pub fn count_good_numbers(n: i64) -> i32 {
        if n == 1 {
            return 5;
        }

        fn pow(mut base: i64, mut exp: i64) -> i64 {
            if exp == 0 {
                return 1;
            }
            let mut ret = 1;
            while exp > 0 {
                if exp % 2 == 0 {
                    base = base * base % 1000000007;
                    exp /= 2;
                } else {
                    ret = ret * base % 1000000007;
                    exp -= 1;
                }
            }
            ret
        }
        let even = (n+1) / 2;
        let odd = n / 2;

        (pow(5, even) * pow(4, odd) % 1000000007) as i32
    }
}

impl Solution {
    pub fn rotated_digits(n: i32) -> i32 {
        fn is_good(mut n: i32) -> bool {
            let org = n;
            let mut arr = Vec::new();
            while n > 0 {
                let d = rotate(n % 10);
                if d == -1 {
                    return false;
                }
                arr.push(d);
                n /= 10;
            }
            let mut num = 0;
            for d in arr.into_iter().rev() {
                num *= 10;
                num += d;
            }
            num != org
        }
        fn rotate(d: i32) -> i32 {
            if d == 0 || d == 1 || d == 8 {
                return d;
            }
            if d == 2 {
                return 5;
            }
            if d == 5 {
                return 2;
            }
            if d == 6 {
                return 9;
            }
            if d == 9 {
                return 6;
            }
            return -1;
        }
        (1..(n+1)).filter(|num| is_good(*num)).count() as i32
    }
}

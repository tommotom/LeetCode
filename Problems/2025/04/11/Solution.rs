impl Solution {
    pub fn count_symmetric_integers(low: i32, high: i32) -> i32 {
        fn is_symmetric(num: i32) -> bool {
            let str_num = num.to_string();
            let l = str_num.len();
            if l % 2 == 1 {
                return false;
            }

            let mut i = 0;
            let mut first = 0;
            let mut second = 0;
            for c in str_num.chars() {
                let n: i32 = c.to_string().parse().unwrap();
                if i < l / 2 {
                    first += n;
                } else {
                    second += n;
                }
                i += 1;
            }
            first == second
        }

        let mut ans = 0;
        for num in low..(high+1) {
            if is_symmetric(num) {
                ans += 1;
            }
        }
        ans
    }
}

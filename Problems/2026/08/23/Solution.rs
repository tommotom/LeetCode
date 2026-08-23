impl Solution {
    pub fn sum_game(num: String) -> bool {
        let n = num.len();
        let mut sum1 = 0;
        let mut sum2 = 0;
        let mut c1 = 0;
        let mut c2 = 0;

        for (i, ch) in num.chars().enumerate() {
            if i < n / 2 {
                if ch == '?' {
                    c1 += 1;
                } else {
                    sum1 += ch.to_digit(10).unwrap() as i32;
                }
            } else {
                if ch == '?' {
                    c2 += 1;
                } else {
                    sum2 += ch.to_digit(10).unwrap() as i32;
                }
            }
        }

        if (c1 + c2) % 2 != 0 {
            return true;
        }

        if sum1 - sum2 == (c2 - c1) / 2 * 9 {
            return false;
        }

        true
    }
}

impl Solution {
    pub fn punishment_number(n: i32) -> i32 {
        let mut ans = 0;
        for i in 1..(n+1) {
            let square = i * i;
            if Self::is_punishment(square, i) {
                ans += square;
            }
        }
        ans
    }

    fn is_punishment(mut square: i32, target: i32) -> bool {
        let mut part = 0;
        let mut d = 1;
        while square > 0 {
            part += square % 10 * d;
            square /= 10;
            d *= 10;
            if target < part {
                return false;
            }
            if square + part == target || Self::is_punishment(square, target - part) {
                return true;
            }
        }
        false
    }
}

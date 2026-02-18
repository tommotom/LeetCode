impl Solution {
    pub fn has_alternating_bits(mut n: i32) -> bool {
        let mut last = n % 2;
        n /= 2;
        while n > 0 {
            if n % 2 == last {
                return false;
            }
            last ^= 1;
            n /= 2;
        }
        true
    }
}

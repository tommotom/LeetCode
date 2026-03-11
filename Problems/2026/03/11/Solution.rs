impl Solution {
    pub fn bitwise_complement(n: i32) -> i32 {
        if n == 0 {
            return 1;
        }
        let mut d = 0;
        let mut num = n;
        while num > 0 {
            num /= 2;
            d *= 2;
            d += 1;
        }
        n ^ d

    }
}

impl Solution {
    pub fn sum_and_multiply(mut n: i32) -> i64 {
        let (mut x, mut sum, mut k) = (0, 0, 1);
        while n > 0 {
            if n % 10 != 0 {
                x += k * (n % 10);
                k *= 10;
                sum += n % 10;
            }
            n /= 10;
            continue;
        }
        x as i64 * sum as i64
    }
}

impl Solution {
    pub fn max_product(mut n: i32) -> i32 {
        let mut digits = Vec::new();
        while n > 0 {
            digits.push(n % 10);
            n /= 10;
        }
        digits.sort();
        let l = digits.len() - 1;
        digits[l] * digits[l-1]
    }
}

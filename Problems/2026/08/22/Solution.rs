impl Solution {
    pub fn check_divisibility(n: i32) -> bool {
        let mut sum = 0;
        let mut product = 1;
        let mut num = n;
        while num > 0 {
            sum += num % 10;
            product *= num % 10;
            num /= 10;
        }
        (n % (sum + product)) == 0
    }
}

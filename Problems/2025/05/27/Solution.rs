impl Solution {
    pub fn difference_of_sums(n: i32, m: i32) -> i32 {
        let mut num1 = 0;
        let mut num2 = 0;
        for num in 1..(n+1) {
            if num % m == 0 {
                num2 += num;
            } else {
                num1 += num;
            }
        }
        num1 - num2
    }
}

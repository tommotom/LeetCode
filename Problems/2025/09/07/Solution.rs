impl Solution {
    pub fn sum_zero(mut n: i32) -> Vec<i32> {
        let mut num = 1;
        let mut ans = Vec::new();
        while n > 1 {
            ans.push(num);
            ans.push(-num);
            n -= 2;
            num += 1;
        }
        if n == 1 {
            ans.push(0);
        }
        ans
    }
}

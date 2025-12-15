impl Solution {
    pub fn get_descent_periods(prices: Vec<i32>) -> i64 {
        let mut ans: i64 = 1;
        let mut d: i64 = 0;
        for i in 1.. prices.len() {
            if prices[i-1] - 1 == prices[i] {
                d += 1;
            } else {
                d = 0;
            }
            ans += 1 + d;
        }
        ans
    }
}

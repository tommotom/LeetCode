impl Solution {
    pub fn count_commas(mut n: i32) -> i32 {
        let mut ans = 0;
        for mut num in 1..=n {
            let mut d = 0;
            while num > 0 {
                num /= 10;
                d += 1;
            }
            ans += (d-1)/3
        }
        ans
    }
}

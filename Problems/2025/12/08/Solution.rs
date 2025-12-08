impl Solution {
    pub fn count_triples(n: i32) -> i32 {
        let mut ans = 0;
        for c in 1..=n {
            let mut a = c - 1;
            for b in 1..c {
                while a * a + b * b > c * c {
                    a -= 1;
                }
                if a * a + b * b == c * c {
                    ans += 1;
                }
            }
        }
        ans
    }
}

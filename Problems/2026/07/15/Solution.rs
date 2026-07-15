impl Solution {
    pub fn gcd_of_odd_even_sums(n: i32) -> i32 {
        let (mut odd, mut even) = (0, 0);
        for num in 0..n {
            odd += 2 * num + 1;
            even += 2 * num + 2;
        }
        let mut ans = 0;
        for d in 1..=odd {
            if odd % d == 0 && even % d == 0 {
                ans = d;
            }
        }
        ans
    }
}

impl Solution {
    pub fn reverse_bits(mut n: i32) -> i32 {
        let mut bits = Vec::new();
        for _ in 0..32 {
            bits.push(n % 2);
            n /= 2;
        }
        bits = bits.into_iter().rev().collect();
        let mut ans = 0;
        for i in 0..bits.len() {
            ans += (1 << i) * bits[i];
        }
        ans
    }
}

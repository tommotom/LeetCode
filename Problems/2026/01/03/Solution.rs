impl Solution {
    pub fn num_of_ways(n: i32) -> i32 {
        const MOD: i64 = 1000000007;
        let mut a: i64 = 6;
        let mut b: i64 = 6;

        for _ in 2..=n {
            let new_a = (2 * a + 2 * b) % MOD;
            let new_b = (2 * a + 3 * b) % MOD;
            a = new_a;
            b = new_b;
        }

        ((a + b) % MOD) as i32
    }
}

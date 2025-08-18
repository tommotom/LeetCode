impl Solution {
    pub fn product_queries(n: i32, queries: Vec<Vec<i32>>) -> Vec<i32> {
        const MOD: i64 = 1_000_000_007;
        let mut bins = Vec::new();
        let mut n = n;
        let mut rep = 1;
        while n > 0 {
            if n % 2 == 1 {
                bins.push(rep);
            }
            n /= 2;
            rep *= 2;
        }

        queries.iter().map(|query| {
            let mut cur: i64 = 1;
            for i in query[0]..=query[1] {
                cur = (cur * bins[i as usize]) % MOD;
            }
            cur as i32
        }).collect()
    }
}

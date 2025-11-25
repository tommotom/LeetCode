impl Solution {
    pub fn smallest_repunit_div_by_k(k: i32) -> i32 {
        let k = k as i64;
        let mut n = 0 as i64;
        for l in 1..100000 {
            n = (n * 10 + 1) % k;
            if n == 0 {
                return l as i32;
            }
        }
        -1
    }
}

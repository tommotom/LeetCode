impl Solution {
    pub fn repair_cars(ranks: Vec<i32>, cars: i32) -> i64 {
        fn isValid(ranks: &Vec<i32>, cars: i32, m: i64) -> bool {
            let mut repaired = 0;
            for rank in ranks {
                repaired += (m / (*rank as i64)).isqrt()
            }
            repaired >= cars as i64
        }

        let mut l = 0;
        let mut r = i64::MAX;
        while l < r {
            let m = l + (r - l) / 2;
            if isValid(&ranks, cars, m) {
                r = m;
            } else {
                l = m + 1;
            }
        }
        l
    }
}

impl Solution {
    pub fn get(num: i32) -> i64 {
        let mut i: i64 = 1;
        let mut base: i64 = 1;
        let mut cnt: i64 = 0;
        let num = num as i64;
        while base <= num {
            cnt += ((i + 1) / 2) * (std::cmp::min(base * 2 - 1, num) - base + 1);
            i += 1;
            base *= 2;
        }
        cnt
    }

    pub fn min_operations(queries: Vec<Vec<i32>>) -> i64 {
        let mut res: i64 = 0;
        for q in queries.iter() {
            let left = q[0] as i32;
            let right = q[1] as i32;
            res += (Self::get(right) - Self::get(left - 1) + 1) / 2;
        }
        res
    }
}

impl Solution {
    pub fn distribute_candies(n: i32, limit: i32) -> i64 {
        if n > limit * 3 {
            return 0;
        }
        let mut ans = 0;
        for a in 0..(n+1) {
            if a > limit {
                break;
            }
            let left = n - a;
            if limit * 2 < left {
                continue;
            }
            let b = (left - limit).max(0);
            ans += (left - 2 * b + 1) as i64;
        }
        ans
    }
}

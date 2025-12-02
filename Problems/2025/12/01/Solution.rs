impl Solution {
    pub fn max_run_time(mut n: i32, mut batteries: Vec<i32>) -> i64 {
        let mut n = n as i64;
        let mut batteries: Vec<i64> = batteries.iter().map(|&x| x as i64).collect();
        let mut total: i64 = batteries.iter().sum();
        batteries.sort();
        for &b in batteries.iter().rev() {
            if b > total / (n as i64) {
                total -= b;
                n -= 1;
            } else {
                break;
            }
        }
        total / n
    }
}

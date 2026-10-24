impl Solution {
    pub fn count_days_together(arrive_alice: String, leave_alice: String, arrive_bob: String, leave_bob: String) -> i32 {
        let dates_per_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31];
        let mut ans = 0;
        for m in 1..=12 {
            for d in 1..=dates_per_month[m - 1] {
                 let mmdd: String = format!("{:02}-{:02}", m, d);
                 if arrive_alice <= mmdd && mmdd <= leave_alice && arrive_bob <= mmdd && mmdd <= leave_bob {
                    ans += 1;
                 }
            }
        }
        ans
    }
}

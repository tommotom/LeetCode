impl Solution {
    pub fn count_days(days: i32, mut meetings: Vec<Vec<i32>>) -> i32 {
        meetings.sort_by(|a, b| if a[0] != b[0] {a[0].cmp(&b[0])} else {b[1].cmp(&a[1])});
        println!("{:?}", meetings);
        let mut ans = 0;
        let mut last = 0;
        for meeting in meetings {
            let start = meeting[0];
            let end = meeting[1];
            if last < start {
                ans += start - last - 1;
            }
            last = last.max(end);
        }
        if last < days {
            ans += days - last;
        }
        ans
    }
}

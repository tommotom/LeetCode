impl Solution {
    pub fn minimum_effort(mut tasks: Vec<Vec<i32>>) -> i32 {
        tasks.sort_by(|a, b| (a[1] - a[0]).cmp(&(b[1] - b[0])));
        let mut ans = 0;
        for task in tasks {
            ans = task[1].max(ans + task[0]);
        }
        ans
    }
}

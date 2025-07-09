impl Solution {
    pub fn max_free_time(event_time: i32, k: i32, start_time: Vec<i32>, end_time: Vec<i32>) -> i32 {
        let n = start_time.len();
        let k = k as usize;
        let mut res: i32 = 0;
        let mut t: i32 = 0;

        for i in 0..n {
            t += end_time[i] - start_time[i];
            let left = if i <= k - 1 { 0 } else { end_time[i-k] };
            let right = if i == n - 1 { event_time } else { start_time[i+1] };
            res = res.max(right - left - t);
            if i >= k - 1 {
                t -= end_time[i-k+1] - start_time[i-k+1];
            }
        }
        res
    }
}

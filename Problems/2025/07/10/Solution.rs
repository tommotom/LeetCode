use std::collections::BinaryHeap;
use std::cmp::Reverse;

impl Solution {
    pub fn max_free_time(event_time: i32, start_time: Vec<i32>, end_time: Vec<i32>) -> i32 {
        let mut free_time = Vec::new();
        let mut last = 0;
        let n = start_time.len();
        for i in 0..n {
            free_time.push(start_time[i] - last);
            last = last.max(end_time[i]);
        }
        free_time.push(event_time - end_time[n-1]);

        let mut f = BinaryHeap::new();
        for i in 0..(n+1) {
            f.push(Reverse((free_time[i], i)));
        }
        while f.len() > 3 {
            f.pop();
        }

        let mut ans = 0;
        for i in 0..n {
            let d = end_time[i] - start_time[i];
            let l = if i == 0 { 0 } else { end_time[i-1] };
            let r = if i == n-1 { event_time } else { start_time[i+1] };
            ans = ans.max(r - l - d);
            for &Reverse((free, j)) in &f {
                if free >= d && j != i && j != i+1 {
                    ans = ans.max(r - l);
                }
            }
        }
        ans
    }
}

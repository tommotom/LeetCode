impl Solution {
    pub fn intersection_size_two(mut intervals: Vec<Vec<i32>>) -> i32 {
        let mut intervals: Vec<Vec<usize>> = intervals.iter().map(|interval| interval.iter().map(|i| *i as usize).collect()).collect();
        intervals.sort_by(|a, b| if a[0] != b[0] {a[0].cmp(&b[0])} else {b[1].cmp(&a[1])});
        let mut todo = vec![2; intervals.len()];
        let mut ans = 0;
        for t in (0..intervals.len()).rev() {
            let s = intervals[t][0];
            let e = intervals[t][1];
            let m = todo[t];
            for p in s..(s+m) {
                for i in 0..=t {
                    if todo[i] > 0 && p <= intervals[i][1] {
                        todo[i] -= 1;
                    }
                }
                ans += 1
            }
        }
        ans
    }
}

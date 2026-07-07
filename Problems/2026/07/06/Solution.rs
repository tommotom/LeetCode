impl Solution {
    pub fn remove_covered_intervals(intervals: Vec<Vec<i32>>) -> i32 {
        fn is_covered(a: &Vec<i32>, b: &Vec<i32>) -> bool {
            b[0] <= a[0] && a[1] <= b[1]
        }
        let mut n = intervals.len();
        let mut covered = vec![false; n];
        for i in 0..n {
            for j in 0..n {
                if i == j {
                    continue;
                }
                if is_covered(&intervals[i], &intervals[j]) {
                    covered[i] = true;
                    break;
                }
            }
        }
        covered.iter().filter(|&a| !a).count() as i32
    }
}

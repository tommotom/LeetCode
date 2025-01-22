use std::collections::VecDeque;

impl Solution {
    pub fn highest_peak(is_water: Vec<Vec<i32>>) -> Vec<Vec<i32>> {
        let m = is_water.len();
        let n = is_water[0].len();
        let mut q = VecDeque::new();
        let mut ans = vec![vec![-1; n]; m];
        for r in 0..m {
            for c in 0..n {
                if is_water[r][c] == 1 {
                    q.push_back((r, c));
                    ans[r][c] = 0;
                }
            }
        }

        let dirs = [[1, 2], [1, 0], [2, 1], [0, 1]];
        while (q.len() > 0) {
            let (r, c) = q.pop_front().unwrap();
            for [dr, dc] in dirs {
                let next_r = r + dr - 1;
                let next_c = c + dc - 1;
                if (next_r == 18446744073709551615 || next_r == m || next_c == 18446744073709551615 || next_c == n) {
                    continue;
                }
                if (ans[next_r][next_c] > -1) {
                    continue;
                }
                ans[next_r][next_c] = ans[r][c] + 1;
                q.push_back((next_r, next_c));
            }
        }
        ans
    }
}

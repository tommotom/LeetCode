use std::collections::BinaryHeap;
use std::collections::HashSet;
use core::cmp::Reverse;

impl Solution {
    pub fn max_points(grid: Vec<Vec<i32>>, queries: Vec<i32>) -> Vec<i32> {
        fn check_neighbors(grid: &Vec<Vec<i32>>, seen: &mut HashSet<(usize, usize)>, q: &mut BinaryHeap<Reverse<(i32, usize, usize)>>, r: usize, c: usize) {
            let m = grid.len();
            let n = grid[0].len();
            if r > 0 && !seen.contains(&(r-1, c)) {
                q.push(Reverse((grid[r-1][c], r-1, c)));
                seen.insert((r-1, c));
            }
            if c > 0 && !seen.contains(&(r, c-1)) {
                q.push(Reverse((grid[r][c-1], r, c-1)));
                seen.insert((r, c-1));
            }
            if r+1 < m && !seen.contains(&(r+1, c)) {
                q.push(Reverse((grid[r+1][c], r+1, c)));
                seen.insert((r+1, c));
            }
            if c+1 < n && !seen.contains(&(r, c+1)) {
                q.push(Reverse((grid[r][c+1], r, c+1)));
                seen.insert((r, c+1));
            }
        }

        let mut q = BinaryHeap::new();
        q.push(Reverse((grid[0][0], 0, 0)));
        let mut seen = HashSet::new();
        seen.insert((0, 0));
        let mut scores = vec![(0, 0)];
        let mut score = 0;
        let mut M = 0;
        while let Some(Reverse((cur, r, c))) = q.pop() {
            check_neighbors(&grid, &mut seen, &mut q, r, c);
            scores.push((cur, score));
            M = M.max(cur);

            while let Some(Reverse((next_cur, next_r, next_c))) = q.pop() {
                if next_cur <= cur {
                    score += 1;
                    check_neighbors(&grid, &mut seen, &mut q, next_r, next_c);
                } else {
                    q.push(Reverse((next_cur, next_r, next_c)));
                    break;
                }
            }
            score += 1;
        }
        scores.push((M+1, score));

        let mut ans = Vec::new();
        for query in queries {
            let mut l = 0;
            let mut r = scores.len();
            while l < r {
                let m = l + (r - l) / 2;
                if scores[m].0 < query {
                    l = m + 1;
                } else {
                    r = m;
                }
            }
            ans.push(scores[l.min(scores.len() - 1)].1);
        }

        ans
    }
}

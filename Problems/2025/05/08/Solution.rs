use std::collections::HashSet;
use std::collections::BinaryHeap;
use std::cmp::Reverse;

impl Solution {
    pub fn min_time_to_reach(move_time: Vec<Vec<i32>>) -> i32 {
        let n = move_time.len();
        let m = move_time[0].len();
        let adj: [(i32, i32); 4] = [(0, 1), (0, -1), (1, 0), (-1, 0)];
        let mut visited = HashSet::new();
        let mut q = BinaryHeap::new();
        visited.insert((0, 0, 0));
        q.push(Reverse((0, 0, 0, 0)));
        while let Some(Reverse((t, x, y, flag))) = q.pop() {
            if x as usize == n-1 && y as usize == m-1 {
                return t;
            }
            for (dx, dy) in adj {
                let next_x = x + dx;
                let next_y = y + dy;
                if next_x < 0 || next_x as usize == n || next_y < 0 || next_y as usize == m {
                    continue;
                }
                if visited.contains(&(next_x, next_y, 1-flag)) {
                    continue;
                }
                visited.insert((next_x, next_y, 1-flag));
                q.push(Reverse((move_time[next_x as usize][next_y as usize].max(t) + 1 + flag, next_x, next_y, 1-flag)));
            }
        }
        0
    }
}

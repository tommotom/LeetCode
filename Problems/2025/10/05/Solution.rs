use std::collections::HashSet;

impl Solution {
    pub fn pacific_atlantic(heights: Vec<Vec<i32>>) -> Vec<Vec<i32>> {
        fn is_valid(r: i32, c: i32, heights: &Vec<Vec<i32>>) -> bool {
            0 <= r && r < heights.len() as i32 && 0 <= c && c < heights[0].len() as i32
        }

        fn dfs(r: i32, c: i32, heights: &Vec<Vec<i32>>, visited: &mut HashSet<(i32, i32)>) {
            visited.insert((r, c));
            for (dr, dc) in [(1, 0), (-1, 0), (0, 1), (0, -1)] {
                let (next_r, next_c) = (r + dr, c + dc);
                if (!is_valid(next_r, next_c, heights)) {
                    continue;
                }
                if heights[r as usize][c as usize] > heights[next_r as usize][next_c as usize] {
                    continue;
                }
                let key = (next_r, next_c);
                if visited.contains(&key) {
                    continue;
                }
                dfs(next_r, next_c, heights, visited);
            }
        }
        let (mut pacific, mut atlantic) = (HashSet::new(), HashSet::new());
        for r in 0..heights.len() as i32 {
            dfs(r, 0, &heights, &mut pacific);
            dfs(r, heights[0].len() as i32 - 1, &heights, &mut atlantic);
        }
        for c in 1..heights[0].len() as i32 {
            dfs(0, c, &heights, &mut pacific);
            dfs(heights.len() as i32 - 1, c - 1, &heights, &mut atlantic);
        }
        let mut ans = Vec::new();
        for r in 0..heights.len() as i32 {
            for c in 0..heights[0].len() as i32 {
                let mut key = (r, c);
                if pacific.contains(&key) && atlantic.contains(&key) {
                    ans.push(vec![r, c]);
                }
            }
        }
        ans
    }
}

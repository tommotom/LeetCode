use std::collections::HashMap;

impl Solution {
    pub fn contains_cycle(grid: Vec<Vec<char>>) -> bool {
        fn is_valid(p: (i32, i32), grid: &Vec<Vec<char>>) -> bool {
            let (r, c) = p;
            0 <= r && r < grid.len() as i32 && 0 <= c && c < grid[0].len() as i32
        }

        fn dfs(p: (i32, i32), visited: &mut HashMap<(i32, i32), i32>, grid: &Vec<Vec<char>>, start: (i32, i32), len: i32) -> bool {
            if visited.contains_key(&p) {
                return len - visited.get(&p).unwrap() >= 4;
            }
            let (r, c) = p;
            visited.insert(p, len);
            for dir in [[1, 0], [-1, 0], [0, 1], [0, -1]] {
                let (next_r, next_c) = (r + dir[0], c + dir[1]);
                if !is_valid((next_r, next_c), grid) {
                    continue;
                }
                if grid[next_r as usize][next_c as usize] == grid[r as usize][c as usize] {
                    if dfs((next_r, next_c), visited, grid, start, len+1) {
                        return true;
                    }
                }
            }
            false
        }

        let mut visited = HashMap::new();
        let (m, n) = (grid.len(), grid[0].len());
        for r in 0..m {
            for c in 0..n {
                let p = (r as i32, c as i32);
                if dfs(p, &mut visited, &grid, p, 1) {
                    return true;
                }
            }
        }

        false
    }
}

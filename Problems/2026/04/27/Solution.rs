use std::collections::HashSet;

impl Solution {
    pub fn has_valid_path(grid: Vec<Vec<i32>>) -> bool {
        fn helper(a: [i32; 2], b: [i32; 2]) -> bool {
            (a[0] == 0 && b[0] == 0 && a[1] != b[1]) || (a[0] != b[0] && a[1] == 0 && b[1] == 0)
        }

        fn dfs(cur: (i32, i32), visited: &mut HashSet<(i32, i32)>, grid: &Vec<Vec<i32>>) -> bool {
            let roads = [[[0, 1],[0, -1]],[[1, 0],[-1, 0]],[[0, -1],[1, 0]],[[1, 0],[0, 1]],[[-1, 0],[0, -1]],[[-1, 0],[0,1]]];
            if visited.contains(&cur) {
                return false;
            }
            visited.insert(cur);
            let (r, c) = cur;
            if r == grid.len() as i32 - 1 && c == grid[0].len() as i32 - 1 {
                return true;
            }
            let road = (grid[r as usize][c as usize]) as usize - 1;
            for ro in roads[road] {
                let (next_r, next_c) = (r + ro[0], c + ro[1]);
                if next_r < 0 || next_r == grid.len() as i32 || next_c < 0 || next_c == grid[0].len() as i32 {
                    continue;
                }
                let next_road = roads[grid[next_r as usize][next_c as usize] as usize - 1];
                if !helper(ro, next_road[0]) && !helper(ro, next_road[1]) {
                    continue;
                }
                if dfs((next_r, next_c), visited, grid) {
                    return true;
                }
            }
            return false;
        }
        dfs((0, 0), &mut HashSet::new(), &grid)
    }
}

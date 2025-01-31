use std::collections::HashSet;

impl Solution {
    pub fn largest_island(mut grid: Vec<Vec<i32>>) -> i32 {
        let n = grid.len();
        let mut ids = Vec::new();
        for i in 0..(n*n) {
            ids.push(i);
        }

        fn find(u: usize, ids: &mut Vec<usize>) -> usize {
            if u != ids[u] {
                ids[u] = find(ids[u], ids);
            }
            ids[u]
        }

        fn union(mut u: usize, mut v: usize, ids: &mut Vec<usize>) {
            u = find(u, ids);
            v = find(v, ids);
            ids[u] = v;
        }

        fn to_id(r: usize, c: usize, n: usize) -> usize {
            c + r * n
        }

        let mut area = vec![0; n*n];
        for r in 0..n {
            for c in 0..n {
                if grid[r][c] == 0 {
                    continue;
                }
                if r+1 < n && grid[r+1][c] == 1 {
                    union(to_id(r, c, n), to_id(r+1, c, n), &mut ids);
                }
                if c+1 < n && grid[r][c+1] == 1 {
                    union(to_id(r, c, n), to_id(r, c+1, n), &mut ids);
                }
            }
        }

        for r in 0..n {
            for c in 0..n {
                let i = to_id(r, c, n);
                ids[i] = find(i, &mut ids);
                area[ids[i]] += grid[r][c];
            }
        }

        let mut ans = *area.iter().max().unwrap();
        for r in 0..n {
            for c in 0..n {
                if grid[r][c] == 1 {
                    continue;
                }
                let mut tmp = 1;
                let mut seen = HashSet::new();
                if r > 0 && grid[r-1][c] == 1 {
                    tmp += area[ids[to_id(r-1, c, n)]];
                    seen.insert(ids[to_id(r-1, c, n)]);
                }
                if c > 0 && grid[r][c-1] == 1 && !seen.contains(&ids[to_id(r, c-1, n)]) {
                    tmp += area[ids[to_id(r, c-1, n)]];
                    seen.insert(ids[to_id(r, c-1, n)]);
                }
                if r+1 < n && grid[r+1][c] == 1 && !seen.contains(&ids[to_id(r+1, c, n)]) {
                    tmp += area[ids[to_id(r+1, c, n)]];
                    seen.insert(ids[to_id(r+1, c, n)]);
                }
                if c+1 < n && grid[r][c+1] == 1 && !seen.contains(&ids[to_id(r, c+1, n)]) {
                    tmp += area[ids[to_id(r, c+1, n)]];
                }
                ans = ans.max(tmp);
            }
        }

        ans
    }
}

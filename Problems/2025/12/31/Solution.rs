struct UnionFind {
    ids: Vec<usize>
}

impl UnionFind {
    fn new(n: usize) -> Self {
        UnionFind {
            ids: (0..n).collect()
        }
    }

    fn find(&mut self, u: usize) -> usize {
        if self.ids[u] != u {
            self.ids[u] = self.find(self.ids[u]);
        }
        self.ids[u]
    }

    fn union(&mut self, mut u: usize, mut v: usize) {
        u = self.find(u);
        v = self.find(v);
        self.ids[u] = v;
    }
}

impl Solution {
    pub fn latest_day_to_cross(row: i32, col: i32, cells: Vec<Vec<i32>>) -> i32 {
        let row = row as usize;
        let col = col as usize;
        let n = row * col + 2;
        let mut uf = UnionFind::new(n);
        for c in 0..col {
            uf.union(0, c + 1);
            uf.union(n - 1, n - c - 2);
        }

        fn to_id(r: usize, c: usize, col: usize) -> usize {
            r * col + c + 1
        }

        let mut ans = cells.len() - 1;
        let mut grid = vec![vec![1; col]; row];

        for cell in cells.into_iter().rev() {
            let r = cell[0] as usize - 1;
            let c = cell[1] as usize - 1;
            grid[r][c] = 0;
            if r > 0 && grid[r-1][c] == 0 {
                uf.union(to_id(r, c, col), to_id(r-1, c, col));
            }
            if c > 0 && grid[r][c-1] == 0 {
                uf.union(to_id(r, c, col), to_id(r, c-1, col));
            }
            if r + 1 < row && grid[r+1][c] == 0 {
                uf.union(to_id(r, c, col), to_id(r+1, c, col));
            }
            if c + 1 < col && grid[r][c+1] == 0 {
                uf.union(to_id(r, c, col), to_id(r, c+1, col));
            }
            if uf.find(0) == uf.find(n-1) {
                return ans as i32;
            }
            ans -= 1;
        }
        ans as i32
    }
}

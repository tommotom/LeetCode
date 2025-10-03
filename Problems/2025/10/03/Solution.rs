struct DisjointSet {
    parent: Vec<usize>,
    size: Vec<usize>,
}

impl Solution {
    const directions: [(i32, i32); 4] = [(-1, 0), (1, 0), (0, -1), (0, 1)];

    pub fn trap_rain_water(height_map: Vec<Vec<i32>>) -> i32 {
        let m = height_map.len();
        let n = height_map[0].len();

        if m < 3 || n < 3 {
            return 0;
        }

        let cell_index = |r: usize, c: usize| -> usize { 1 + r * n + c };

        let to_valid_cell = |r: i32, c: i32| -> Option<(usize, usize)> {
            if (0..m as i32).contains(&r) && (0..n as i32).contains(&c) {
                Some((r as usize, c as usize))
            } else {
                None
            }
        };

        let is_boundary_cell = |r: usize, c: usize| r == 0 || r == m - 1 || c == 0 || c == n - 1;

        let mut cells = Vec::new();
        for r in 0..m {
            for c in 0..n {
                cells.push((height_map[r][c], r, c));
            }
        }

        cells.sort_by_key(|&(h, _, _)| h);

        let mut ds = DisjointSet::new(m * n + 1);
        let boundary = 0;
        let mut volume = 0;
        let mut prev_height = 0;

        for (i, (h, r, c)) in cells.into_iter().enumerate() {
            if h > prev_height {
                let boundary_size = ds.component_size(boundary);
                let inner_cells = (i + 1 - boundary_size) as i32;

                volume += (h - prev_height) * inner_cells;
                prev_height = h;
            }

            for &(dr, dc) in &Self::directions {
                if let Some((nr, nc)) = to_valid_cell(r as i32 + dr, c as i32 + dc) {
                    if height_map[nr][nc] <= h {
                        ds.union(cell_index(r, c), cell_index(nr, nc));
                    }
                }
            }

            if is_boundary_cell(r, c) {
                ds.union(boundary, cell_index(r, c));
            }
        }

        volume
    }
}

impl DisjointSet {
    fn new(n: usize) -> Self {
        let parent = (0..n).collect();
        let size = vec![1; n];
        Self { parent, size }
    }

    fn find(&mut self, v: usize) -> usize {
        if self.parent[v] != v {
            self.parent[v] = self.find(self.parent[v]);
        }
        self.parent[v]
    }

    fn union(&mut self, a: usize, b: usize) {
        let root_a = self.find(a);
        let root_b = self.find(b);
        if root_a != root_b {
            if self.size[root_a] < self.size[root_b] {
                self.parent[root_a] = root_b;
                self.size[root_b] += self.size[root_a];
            } else {
                self.parent[root_b] = root_a;
                self.size[root_a] += self.size[root_b];
            }
        }
    }

    fn component_size(&mut self, v: usize) -> usize {
        let root = self.find(v);
        self.size[root]
    }
}

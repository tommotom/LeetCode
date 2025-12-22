struct UnionFind {
    parent: Vec<usize>,
    rank: Vec<usize>,
}

impl UnionFind {
    fn new(n: usize) -> Self {
        Self {
            parent: (0..n).collect(),
            rank: vec![0; n],
        }
    }

    fn reset(&mut self, a: usize) {
        self.parent[a] = a;
        self.rank[a] = 0;
    }

    fn find(&mut self, a: usize) -> usize {
        if self.parent[a] == a {
            return a;
        }

        self.parent[a] = self.find(self.parent[a]);

        self.parent[a]
    }

    fn union(&mut self, a: usize, b: usize) {
        let a = self.find(a);
        let b = self.find(b);

        if a == b {
            return;
        }

        let (child, parent) = match self.rank[a] < self.rank[b] {
            true => (a, b),
            false => (b, a),
        };

        if self.rank[parent] == self.rank[child] {
            self.rank[parent] += 1;
        }

        self.parent[child] = parent;
    }
}

impl Solution {
    pub fn find_all_people(n: i32, meetings: Vec<Vec<i32>>, first_person: i32) -> Vec<i32> {
        let n = n as usize;

        let mut uf = UnionFind::new(n);
        uf.union(0, first_person as usize);

        let mut meetings = meetings;
        meetings.sort_unstable_by_key(|x| x[2]);

        for chunk in meetings.chunk_by(|a, b| a[2] == b[2]) {
            for meeting in chunk {
                let (a, b) = (meeting[0] as usize, meeting[1] as usize);

                uf.union(a, b);
            }

            let secret_root = uf.find(0);

            for meeting in chunk {
                let (a, b) = (meeting[0] as usize, meeting[1] as usize);

                if uf.find(a) != secret_root {
                    uf.reset(a);
                    uf.reset(b);
                }
            }
        }

        let secret_root = uf.find(0);

        (0..n)
            .filter(|&x| uf.find(x) == secret_root)
            .map(|x| x as i32)
            .collect()
    }
}

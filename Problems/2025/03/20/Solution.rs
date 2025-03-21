struct DSU {
    parents: Vec<i32>,
    ranks: Vec<i32>,
    distances: Vec<i32>
}

impl DSU {
    fn new(n: i32) -> Self {
        Self {
            parents: (0..n).collect(),
            ranks: vec![0; n as usize],
            distances: vec![-1; n as usize],
        }
    }

    fn find(&mut self, a: i32) -> i32 {
        if self.parents[a as usize] != a {
            self.parents[a as usize] = self.find(self.parents[a as usize]);
        }
        self.parents[a as usize]
    }

    fn union(&mut self, a: i32, b: i32, weight: i32) {
        let a = self.find(a);
        let b = self.find(b);

        let dist = self.distances[a as usize] & self.distances[b as usize] & weight;
        self.distances[a as usize] = dist;
        self.distances[b as usize] = dist;

        if a == b {
            return;
        }

        if self.ranks[a as usize] < self.ranks[b as usize] {
            self.parents[a as usize] = b;
        } else if self.ranks[a as usize] > self.ranks[b as usize] {
            self.parents[b as usize] = a;
        } else {
            self.ranks[a as usize] += 1;
            self.parents[b as usize] = a;
        }
    }

    fn dist(&mut self, a: i32, b: i32) -> i32 {
        let a = self.find(a);
        if a != self.find(b) {
            return -1;
        }
        self.distances[a as usize]
    }
}

impl Solution {
    pub fn minimum_cost(n: i32, edges: Vec<Vec<i32>>, query: Vec<Vec<i32>>) -> Vec<i32> {
        let mut dsu = DSU::new(n);
        for e in edges {
            dsu.union(e[0], e[1], e[2]);
        }
        query.into_iter().map(|q| dsu.dist(q[0], q[1])).collect()
    }
}

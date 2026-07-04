use std::cmp::Ordering;

struct DSU {
    parents: Vec<i32>,
    ranks: Vec<i32>,
}

impl DSU {
    fn new(n: i32) -> Self {
        Self {
            parents: (0..=n).collect(),
            ranks: vec![0; n as usize + 1],
        }
    }

    fn find(&mut self, a: i32) -> i32 {
        if self.parents[a as usize] != a {
            self.parents[a as usize] = self.find(self.parents[a as usize]);
        }
        self.parents[a as usize]
    }

    fn union(&mut self, mut a: i32, mut b: i32) {
        a = self.find(a);
        b = self.find(b);

        if a == b {
            return;
        }

        match self.ranks[a as usize].cmp(&self.ranks[b as usize]) {
            Ordering::Less => self.parents[a as usize] = b,
            Ordering::Greater => self.parents[b as usize] = a,
            Ordering::Equal => {
                self.ranks[a as usize] += 1;
                self.parents[b as usize] = a;
            }
        }
    }
}

impl Solution {
    pub fn min_score(n: i32, mut roads: Vec<Vec<i32>>) -> i32 {
        let mut dsu = DSU::new(n);
        for r in &roads {
            dsu.union(r[0], r[1]);
        }

        let mut ans = i32::MAX;

        let start = dsu.find(1);
        for r in &roads {
            let end = dsu.find(r[0]);
            if start == end {
                ans = ans.min(r[2]);
            }
        }
        ans
    }
}

use std::collections::HashMap;


pub struct UnionFind {
    parent: Vec<usize>,
    size: Vec<usize>,
}

impl UnionFind {
    pub fn new(n: usize) -> Self {
        UnionFind {
            parent: (0..n).collect(),
            size: vec![1; n],
        }
    }

    pub fn find(&mut self, x: usize) -> usize {
        if self.parent[x] == x {
            x
        } else {
            let p = self.parent[x];
            let root = self.find(p);
            self.parent[x] = root;
            root
        }
    }

    pub fn unite(&mut self, x: usize, y: usize) -> bool {
        let mut root_x = self.find(x);
        let mut root_y = self.find(y);

        if root_x == root_y {
            return false;
        }

        if self.size[root_x] < self.size[root_y] {
            std::mem::swap(&mut root_x, &mut root_y);
        }

        self.parent[root_y] = root_x;
        self.size[root_x] += self.size[root_y];
        true
    }

    pub fn same(&mut self, x: usize, y: usize) -> bool {
        self.find(x) == self.find(y)
    }

    pub fn size(&mut self, x: usize) -> usize {
        let root = self.find(x);
        self.size[root]
    }
}

impl Solution {
    pub fn lexicographically_smallest_array(mut nums: Vec<i32>, limit: i32) -> Vec<i32> {
        let n = nums.len();
        let mut sorted_nums: Vec<(usize, i32)> = nums.iter().cloned().enumerate().collect();
        sorted_nums.sort_by(|a, b| a.1.cmp(&b.1));
        let mut uf = UnionFind::new(n);
        for i in 1..n {
            if sorted_nums[i].1 - sorted_nums[i-1].1 <= limit {
                uf.unite(sorted_nums[i].0, sorted_nums[i-1].0);
            }
        }
        let mut map: HashMap<usize, Vec<i32>> = HashMap::new();
        for i in 0..n {
            map.entry(uf.find(i)).or_insert(Vec::new()).push(nums[i]);
        }

        for vec in map.values_mut() {
            vec.sort_by(|a, b| b.cmp(&a));
        }

        let mut ans = Vec::new();
        for i in 0..n {
            let mut vec = map.get_mut(&uf.find(i)).unwrap();
            ans.push(vec.pop().unwrap());
        }
        ans
    }
}

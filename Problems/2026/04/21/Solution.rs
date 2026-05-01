use std::collections::HashMap;

struct UnionFind {
    parent: Vec<usize>,
    rank: Vec<usize>,
    groups: usize,
}

impl UnionFind {
    // 初期化: 各要素が自分自身を親とする n 個の集合を作成
    fn new(n: usize) -> Self {
        UnionFind {
            parent: (0..n).collect(),
            rank: vec![0; n],
            groups: n,
        }
    }

    // 根（代表元）を見つける（経路圧縮付き）
    fn find(&mut self, i: usize) -> usize {
        if self.parent[i] == i {
            i
        } else {
            // 再帰的に親を辿り、直接根に繋ぎ直す
            let root = self.find(self.parent[i]);
            self.parent[i] = root;
            root
        }
    }

    // 2つの集合を併合する（ランクによる最適化付き）
    fn unite(&mut self, i: usize, j: usize) -> bool {
        let mut root_i = self.find(i);
        let mut root_j = self.find(j);

        if root_i != root_j {
            // 低い方の木を高い方の木に繋ぐ
            if self.rank[root_i] < self.rank[root_j] {
                std::mem::swap(&mut root_i, &mut root_j);
            }
            self.parent[root_j] = root_i;
            if self.rank[root_i] == self.rank[root_j] {
                self.rank[root_i] += 1;
            }
            self.groups -= 1;
            return true; // 併合成功
        }
        false // すでに同じ集合
    }

    // 同じ集合に属しているか判定
    fn is_same(&mut self, i: usize, j: usize) -> bool {
        self.find(i) == self.find(j)
    }
}

impl Solution {
    pub fn minimum_hamming_distance(source: Vec<i32>, target: Vec<i32>, allowed_swaps: Vec<Vec<i32>>) -> i32 {
        let n = source.len();
        let mut uf = UnionFind::new(n);
        for swap in allowed_swaps {
            uf.unite(swap[0] as usize, swap[1] as usize);
        }

        let mut roots = vec![0; n];
        for i in 0..n {
            roots[i] = uf.find(i);
        }

        let mut counter: HashMap<usize, HashMap<i32, i32>> = HashMap::new();
        for i in 0..n {
            *counter.entry(roots[i]).or_default().entry(target[i]).or_insert(0) += 1;;
        }
        let mut ans = 0;
        for i in 0..n {
            if let Some(count) = counter.get_mut(&roots[i]) {
                let entry = count.entry(source[i]).or_insert(0);
                if *entry > 0 {
                    *entry -= 1;
                } else {
                    ans += 1;
                }
            }
        }

        ans
    }
}

struct UF {
    ids: Vec<usize>
}

impl UF {
    fn new(n: i32) -> Self {
        UF {ids: (0..(n as usize)).collect()}
    }

    fn find(&mut self, u: usize) -> usize {
        if (self.ids[u] != u) {
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

use std::collections::HashSet;
use std::collections::HashMap;

impl Solution {
    pub fn count_complete_components(n: i32, edges: Vec<Vec<i32>>) -> i32 {
        fn isComplete(subgraph: &Vec<usize>, graph: &HashMap<usize, HashSet<usize>>) -> bool {
            for i in 0..(subgraph.len()-1) {
                for j in (i+1)..subgraph.len() {
                    if !graph.get(&subgraph[i]).unwrap().contains(&subgraph[j]) {
                        return false;
                    }
                }
            }
            true
        }
        let mut uf = UF::new(n);
        let mut graph = HashMap::new();
        for edge in edges {
            let a = edge[0] as usize;
            let b = edge[1] as usize;
            uf.union(a, b);
            graph.entry(a).or_insert(HashSet::new()).insert(b);
            graph.entry(b).or_insert(HashSet::new()).insert(a);
        }
        let mut subgraphs = HashMap::new();
        for i in 0..(n as usize) {
            uf.ids[i] = uf.find(i);
            subgraphs.entry(uf.ids[i]).or_insert(Vec::new()).push(i);
        }
        let mut ans = 0;
        for (id, subgraph) in subgraphs.into_iter() {
            if isComplete(&subgraph, &graph) {
                ans += 1;
            }
        }
        ans
    }
}

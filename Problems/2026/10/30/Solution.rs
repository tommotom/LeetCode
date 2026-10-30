use std::collections::BinaryHeap;
use std::cmp::Reverse;

impl Solution {
    pub fn shortest_path(n: i32, edges: Vec<Vec<i32>>, labels: String, k: i32) -> i32 {
        let n = n as usize;
        let k = k as usize;
        if n == 1 { return 0; }
        if k == 0 { return -1; }

        let labels = labels.as_bytes();
        let mut adj: Vec<Vec<(usize, i64)>> = vec![vec![]; n];
        for e in &edges {
            let (u, v, w) = (e[0] as usize, e[1] as usize, e[2] as i64);
            adj[u].push((v, w));
        }

        let mut dist = vec![vec![i64::MAX; k + 1]; n];
        dist[0][1] = 0;
        let mut pq = BinaryHeap::new();
        pq.push(Reverse((0i64, 0usize, 1usize)));

        while let Some(Reverse((d, u, c))) = pq.pop() {
            if d > dist[u][c] { continue; }
            if u == n - 1 { return d as i32; }
            for &(v, w) in &adj[u] {
                let nc = if labels[u] == labels[v] { c + 1 } else { 1 };
                if nc > k { continue; }
                let nd = d + w;
                if nd < dist[v][nc] {
                    dist[v][nc] = nd;
                    pq.push(Reverse((nd, v, nc)));
                }
            }
        }
        -1
    }
}

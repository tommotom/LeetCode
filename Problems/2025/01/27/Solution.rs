use std::cmp::Reverse;
use std::collections::BinaryHeap;

impl Solution {
    pub fn modified_graph_edges(n: i32, mut edges: Vec<Vec<i32>>, source: i32, destination: i32, target: i32) -> Vec<Vec<i32>> {
        let mut adj = vec![Vec::<(usize, usize, i32)>::new(); n as usize];
        for (i, v) in edges.iter().enumerate() {
            adj[v[0] as usize].push((v[1] as usize, i, v[2]));
            adj[v[1] as usize].push((v[0] as usize, i, v[2]));
        }

        let mut dist = vec![i32::MAX; n as usize];
        dist[source as usize] = 0;
        let mut heap =
            BinaryHeap::<(Reverse<(i32, i32)>, Vec<usize>, u128, usize)>::new();
        heap.push((Reverse((0, 0)), Vec::new(), 1 << source, source as usize));
        while let Some((Reverse((c, d)), v, visited, a)) = heap.pop() {
            if d > dist[a] {
                continue;
            }
            if a == destination as usize {
                if c == 0 && d < target {
                    break;
                }
                else {
                    if c != 0 {
                        edges[v[0]][2] = 1 + target - d;
                        for &i in v.iter().skip(1) {
                            edges[i][2] = 1;
                        }
                    }
                    for i in 0..edges.len() {
                        if edges[i][2] == -1 {
                            edges[i][2] = target + 1;
                        }
                    }
                    return edges;
                }
            }
            for &(b, i, w) in adj[a].iter() {
                let bit = 1 << b;
                if visited & bit == bit {
                    continue;
                }
                let visited2 = visited | bit;
                let c2 = c + if w == -1 { 1 } else { 0 };
                let d2 = d + if w == -1 { 1 } else { w };
                if d2 > target {
                    continue;
                }
                if c2 == 0 {
                    if d2 >= dist[b] {
                        continue;
                    }
                    dist[b] = d2;
                }
                else {
                    if d2 > dist[b] {
                        continue;
                    }
                }
                let mut v2 = v.clone();
                if w == -1 {
                    v2.push(i);
                }
                heap.push((Reverse((c2, d2)), v2, visited2, b));
            }
        }
        Vec::new()
    }
}

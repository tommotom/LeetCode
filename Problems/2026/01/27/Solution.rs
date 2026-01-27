use std::collections::{HashMap, BinaryHeap};
use std::cmp::Ordering;

#[derive(Copy, Clone, Eq, PartialEq)]
struct State {
    cost: i32,
    position: i32,
}

impl Ord for State {
    fn cmp(&self, other: &Self) -> Ordering {
        other.cost.cmp(&self.cost)
    }
}

impl PartialOrd for State {
    fn partial_cmp(&self, other: &Self) -> Option<Ordering> {
        Some(self.cmp(other))
    }
}

impl Solution {
    pub fn min_cost(n: i32, edges: Vec<Vec<i32>>) -> i32 {
        let mut graph = HashMap::new();
        for edge in edges {
            let (u, v, w) = (edge[0], edge[1], edge[2]);
            graph.entry(u).or_insert(Vec::new()).push((v, w));
            graph.entry(v).or_insert(Vec::new()).push((u, 2 * w));
        }

        let mut dist: Vec<i32> = vec![i32::MAX; n as usize];
        let mut pq = BinaryHeap::new();

        dist[0] = 0;
        pq.push(State { cost: 0, position: 0 });

        while let Some(State { cost, position }) = pq.pop() {
            if position == n - 1 { return cost; }

            if cost > dist[position as usize] { continue; }

            if let Some(neighbors) = graph.get(&position) {
                for &(next, weight) in neighbors {
                    let next_cost = cost + weight;
                    if next < n && next_cost < dist[next as usize] {
                        dist[next as usize] = next_cost;
                        pq.push(State { cost: next_cost, position: next });
                    }
                }
            }
        }

        if dist[(n - 1) as usize] == i32::MAX { -1 } else { dist[(n - 1) as usize] }
    }
}

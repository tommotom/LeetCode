use std::collections::BinaryHeap;
use std::collections::HashMap;
use std::collections::HashSet;
use core::cmp::Reverse;

impl Solution {
    pub fn count_paths(n: i32, roads: Vec<Vec<i32>>) -> i32 {
        if n == 1 {
            return 1;
        }

        let mut graph = HashMap::new();
        for road in roads {
            let u = road[0];
            let v = road[1];
            let time = road[2] as i64;
            graph.entry(u).or_insert(HashMap::new()).insert(v, time);
            graph.entry(v).or_insert(HashMap::new()).insert(u, time);
        }
        let mut times = vec![i64::MAX; n as usize];
        times[0] = 0;
        let mut q = BinaryHeap::new();
        q.push(Reverse((0, 0)));
        while let Some(Reverse((cur, u))) = q.pop() {
            for (v, t) in graph.get(&u).unwrap().into_iter() {
                if times[*v as usize] > times[u as usize] + *t {
                    times[*v as usize] = times[u as usize] + *t;
                    q.push(Reverse((times[*v as usize], *v)));
                }
            }
        }

        let m = 1000000007;
        let mut ways = vec![0; n as usize];
        let mut visited = HashSet::new();
        ways[0] = 1;
        q = BinaryHeap::new();
        q.push(Reverse((0, 0)));
        while let Some(Reverse((cur, u))) = q.pop() {
            if visited.contains(&u) {
                continue;
            }
            visited.insert(u);
            for (v, t) in graph.get(&u).unwrap().into_iter() {
                if times[*v as usize] == times[u as usize] + *t {
                    ways[*v as usize] = (ways[*v as usize] + ways[u as usize]) % m;
                    q.push(Reverse((times[*v as usize], *v)));
                }
            }
        }
        ways[(n-1) as usize]
    }
}

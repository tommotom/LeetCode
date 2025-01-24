use std::collections::VecDeque;
use std::collections::HashSet;

impl Solution {
    pub fn eventual_safe_nodes(graph: Vec<Vec<i32>>) -> Vec<i32> {
        let n = graph.len();
        let mut set_graph: Vec<HashSet<i32>> = graph.clone().into_iter().map(|g| HashSet::<i32>::from_iter(g.iter().cloned())).collect();
        let mut rev = vec![Vec::new(); n];
        let mut q = VecDeque::new();
        for u in 0..n {
            if graph[u].len() == 0 {
                q.push_back(u);
            }
            for v in &graph[u] {
                rev[*v as usize].push(u);
            }
        }

        let mut ans = Vec::new();
        while q.len() > 0 {
            let u = q.pop_front().unwrap();
            ans.push(u as i32);
            for v in &rev[u] {
                set_graph[*v as usize].remove(&(u as i32));
                if set_graph[*v as usize].len() == 0 {
                    q.push_back(*v as usize);
                }
            }
        }
        ans.sort();
        ans
    }
}

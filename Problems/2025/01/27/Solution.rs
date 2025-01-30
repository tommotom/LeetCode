use std::collections::VecDeque;
use std::collections::HashMap;
use std::collections::HashSet;

impl Solution {
    pub fn check_if_prerequisite(num_courses: i32, prerequisites: Vec<Vec<i32>>, queries: Vec<Vec<i32>>) -> Vec<bool> {
        let n = num_courses as usize;

        let mut graph = vec![Vec::new(); n];
        let mut indeg = vec![0; n];

        for edge in prerequisites {
            let u = edge[0] as usize;
            let v = edge[1] as usize;
            graph[u].push(v);
            indeg[v] += 1;
        }

        let mut dep = vec![HashSet::new(); n];

        let mut queue = VecDeque::new();
        for i in 0..n {
            if indeg[i] == 0 {
                queue.push_back(i);
            }
        }

        while let Some(u) = queue.pop_front() {
            let parents_of_u: Vec<_> = dep[u].iter().copied().collect();

            for &v in &graph[u] {
                for pre in &parents_of_u {
                    dep[v].insert(*pre);
                }

                dep[v].insert(u);

                indeg[v] -= 1;
                if indeg[v] == 0 {
                    queue.push_back(v);
                }
            }
        }

        queries.into_iter().map(|q| {
            let a = q[0] as usize;
            let b = q[1] as usize;
            dep[b].contains(&a)
        }).collect()
    }
}

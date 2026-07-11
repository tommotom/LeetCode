use std::collections::HashMap;

impl Solution {
    pub fn count_complete_components(n: i32, edges: Vec<Vec<i32>>) -> i32 {
        let mut graph = HashMap::new();
        for e in edges {
            graph.entry(e[0]).or_insert(Vec::new()).push(e[1]);
            graph.entry(e[1]).or_insert(Vec::new()).push(e[0]);
        }
        fn dfs(cur: i32, ids: &mut Vec<i32>, id: i32, visited: &mut Vec<bool>, graph: &HashMap<i32, Vec<i32>>) {
            let i = cur as usize;
            ids[i] = id;
            visited[i] = true;
            for next in graph.get(&cur).unwrap_or(&Vec::new()) {
                let j = *next as usize;
                if !visited[j] {
                    dfs(*next, ids, id, visited, graph);
                }
            }
        }
        let mut ids: Vec<i32> = (0..n).collect();
        let mut visited = vec![false; n as usize];
        for cur in 0..n {
            let i = cur as usize;
            if !visited[i] {
                dfs(cur, &mut ids, cur, &mut visited, &graph);
            }
        }

        fn is_complete(id: i32, ids: &mut Vec<i32>, graph: &HashMap<i32, Vec<i32>>, seen: &mut Vec<bool>) -> bool {
            let mut count = ids.iter().filter(|&i| *i == id).count();
            let mut is_complete = true;
            for i in 0..ids.len() {
                let cur = i as i32;
                if ids[i] == id {
                    seen[i] = true;
                    if graph.get(&cur).unwrap_or(&Vec::new()).len() != count - 1 {
                        is_complete = false;
                    }
                }
            }
            is_complete
        }
        let mut seen = vec![false; n as usize];
        let mut ans = 0;
        for id in 0..n {
            if !seen[id as usize] && is_complete(id, &mut ids, &graph, &mut seen) {
                ans += 1;
            }
        }
        ans
    }
}

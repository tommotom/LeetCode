impl Solution {
    pub fn max_target_nodes(edges1: Vec<Vec<i32>>, edges2: Vec<Vec<i32>>, k: i32) -> Vec<i32> {
        let n = edges1.len() + 1; let m = edges2.len() + 1;
        let mut graph1: Vec<Vec<i32>> = vec![vec![]; n]; let mut graph2: Vec<Vec<i32>> = vec![vec![]; m];
        for edge in edges1 {
            graph1[edge[0] as usize].push(edge[1]);
            graph1[edge[1] as usize].push(edge[0]);
        }
        for edge in edges2 {
            graph2[edge[0] as usize].push(edge[1]);
            graph2[edge[1] as usize].push(edge[0]);
        }

        fn count_nodes_within(dist: i32, n: usize, from: i32, graph: &Vec<Vec<i32>>) -> i32 {
            let mut seen = vec![false; n];
            let mut st = vec![[from, 0]];
            let mut ret = 0;
            while st.len() > 0 {
                let cur = st.pop().unwrap();
                if seen[cur[0] as usize] || cur[1] > dist {
                    continue;
                }
                seen[cur[0] as usize] = true;
                ret += 1;
                for next in &graph[cur[0] as usize] {
                    if !seen[*next as usize] {
                        st.push([*next, cur[1] + 1]);
                    }
                }
            }
            ret
        }

        let mut max = 0;
        for i in 0..m {
            max = max.max(count_nodes_within(k-1, m, i as i32, &graph2));
        }

        let mut ans = Vec::new();
        for i in 0..n {
            ans.push(max + count_nodes_within(k, n, i as i32, &graph1));
        }
        ans
    }
}

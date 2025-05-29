impl Solution {
    pub fn max_target_nodes(edges1: Vec<Vec<i32>>, edges2: Vec<Vec<i32>>) -> Vec<i32> {
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

        fn colorize(n: usize, graph: &Vec<Vec<i32>>) -> Vec<i32> {
            let mut seen = vec![false; n];
            let mut color = vec![0; n];
            let mut st = vec![0];
            while st.len() > 0 {
                let cur = st.pop().unwrap();
                if seen[cur as usize] {
                    continue;
                }
                seen[cur as usize] = true;
                for next in &graph[cur as usize] {
                    if !seen[*next as usize] {
                        st.push(*next);
                        color[*next as usize] = 1 - color[cur as usize];
                    }
                }
            }
            color
        }

        let color1 = colorize(n, &graph1);
        let color2 = colorize(m, &graph2);
        let sum1: i32 = color1.clone().into_iter().sum();
        let sum2: i32 = color2.into_iter().sum();
        let score2 = sum2.max(m as i32 - sum2);

        let mut ans = vec![];
        for i in 0..n {
            ans.push(if color1[i] == 0 { n as i32 - sum1 + score2 } else { sum1 + score2 })
        }
        ans
    }
}

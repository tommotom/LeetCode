impl Solution {
    pub fn assign_edge_weights(edges: Vec<Vec<i32>>, queries: Vec<Vec<i32>>) -> Vec<i32> {
        const MOD: i64 = 1_000_000_007;

        let n = edges.len() + 1;
        let mut graph = vec![Vec::<usize>::new(); n + 1];

        for edge in edges {
            let u = edge[0] as usize;
            let v = edge[1] as usize;

            graph[u].push(v);
            graph[v].push(u);
        }

        let mut log = 1usize;
        while (1usize << log) <= n {
            log += 1;
        }

        let mut up = vec![vec![0usize; n + 1]; log];
        let mut depth = vec![0usize; n + 1];

        let mut stack = vec![1usize];

        while let Some(node) = stack.pop() {
            for &next in &graph[node] {
                if next == up[0][node] {
                    continue;
                }

                up[0][next] = node;
                depth[next] = depth[node] + 1;
                stack.push(next);
            }
        }

        for j in 1..log {
            for node in 1..=n {
                up[j][node] = up[j - 1][up[j - 1][node]];
            }
        }

        let mut pow2 = vec![0i32; n + 1];
        pow2[0] = 1;

        for i in 1..=n {
            pow2[i] = ((pow2[i - 1] as i64 * 2) % MOD) as i32;
        }

        fn lca(
            mut a: usize,
            mut b: usize,
            depth: &[usize],
            up: &[Vec<usize>],
            log: usize,
        ) -> usize {
            if depth[a] < depth[b] {
                std::mem::swap(&mut a, &mut b);
            }

            let diff = depth[a] - depth[b];

            for j in 0..log {
                if ((diff >> j) & 1) == 1 {
                    a = up[j][a];
                }
            }

            if a == b {
                return a;
            }

            for j in (0..log).rev() {
                if up[j][a] != up[j][b] {
                    a = up[j][a];
                    b = up[j][b];
                }
            }

            up[0][a]
        }

        let mut answer = Vec::with_capacity(queries.len());

        for query in queries {
            let u = query[0] as usize;
            let v = query[1] as usize;

            let ancestor = lca(u, v, &depth, &up, log);
            let distance = depth[u] + depth[v] - 2 * depth[ancestor];

            if distance == 0 {
                answer.push(0);
            } else {
                answer.push(pow2[distance - 1]);
            }
        }

        answer
    }
}

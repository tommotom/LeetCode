use std::collections::VecDeque;

impl Solution {
    pub fn max_k_divisible_components(
        n: i32,
        edges: Vec<Vec<i32>>,
        values: Vec<i32>,
        k: i32,
    ) -> i32 {
        let n = n as usize;
        let k = k as i64;

        let mut g = vec![Vec::<usize>::new(); n];
        for e in edges {
            let a = e[0] as usize;
            let b = e[1] as usize;
            g[a].push(b);
            g[b].push(a);
        }

        let root = 0usize;
        let mut parent = vec![n; n];
        let mut children_count = vec![0usize; n];
        let mut q = VecDeque::new();
        q.push_back(root);
        parent[root] = n;

        while let Some(u) = q.pop_front() {
            for &v in &g[u] {
                if v == parent[u] {
                    continue;
                }
                parent[v] = u;
                children_count[u] += 1;
                q.push_back(v);
            }
        }

        let mut sum: Vec<i64> = values.into_iter().map(|v| (v as i64) % k).collect();

        let mut leaves = VecDeque::new();
        for i in 0..n {
            if i != root && children_count[i] == 0 {
                leaves.push_back(i);
            }
        }

        let mut ans = 0;

        while let Some(v) = leaves.pop_front() {
            let p = parent[v];
            if p == n {
                continue;
            }

            if sum[v] % k == 0 {
                ans += 1;
            } else {
                sum[p] = (sum[p] + sum[v]) % k;
            }

            if children_count[p] > 0 {
                children_count[p] -= 1;
                if p != root && children_count[p] == 0 {
                    leaves.push_back(p);
                }
            }
        }

        if sum[root] % k == 0 {
            ans += 1;
        }

        ans
    }
}

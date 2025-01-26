use std::collections::VecDeque;

impl Solution {
    pub fn maximum_invitations(favorite: Vec<i32>) -> i32 {
        let n = favorite.len();
        let mut in_degree = vec![0; n];

        for i in 0..n {
            in_degree[favorite[i] as usize] += 1;
        }

        let mut q = VecDeque::new();
        for i in 0..n {
            if in_degree[i] == 0 {
                q.push_back(i);
            }
        }

        let mut depth = vec![1; n];

        while q.len() > 0 {
            let u = q.pop_front().unwrap();
            let v = favorite[u] as usize;
            depth[v] = depth[v].max(depth[u] + 1);
            in_degree[v] -= 1;
            if in_degree[v] == 0 {
                q.push_back(v);
            }
        }

        let mut longest_cycle = 0;
        let mut two_cycle_invitations = 0;

        for i in 0..n {
            if in_degree[i] == 0 {
                continue;
            }
            let mut cycle_length = 0;
            let mut cur = i;
            while in_degree[cur] != 0 {
                in_degree[cur] = 0;
                cycle_length += 1;
                cur = favorite[cur] as usize;
            }

            if cycle_length == 2 {
                two_cycle_invitations += depth[i] + depth[favorite[i] as usize];
            } else {
                longest_cycle = longest_cycle.max(cycle_length);
            }
        }

        longest_cycle.max(two_cycle_invitations)
    }
}

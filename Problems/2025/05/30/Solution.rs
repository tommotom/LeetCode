impl Solution {
    pub fn closest_meeting_node(edges: Vec<i32>, node1: i32, node2: i32) -> i32 {
        let n = edges.len();

        fn dfs(edges: &Vec<i32>, cur: i32, dist: &mut Vec<i32>) {
            if cur == -1 {
                return;
            }
            let next = edges[cur as usize];
            if next == -1 || (dist[next as usize] != -1 && dist[next as usize] <= dist[cur as usize] + 1) {
                return;
            }
            dist[next as usize] = dist[cur as usize] + 1;
            dfs(edges, next, dist);
        }

        let mut dist1 = vec![-1; n];
        dist1[node1 as usize] = 0;
        dfs(&edges, node1, &mut dist1);

        let mut dist2 = vec![-1; n];
        dist2[node2 as usize] = 0;
        dfs(&edges, node2, &mut dist2);

        let mut min = i32::MAX;
        let mut ans = -1;
        for i in 0..n {
            if dist1[i] > -1 && dist2[i] > -1 && min > dist1[i].max(dist2[i]) {
                min = dist1[i].max(dist2[i]);
                ans = i as i32;
            }
        }
        ans
    }
}

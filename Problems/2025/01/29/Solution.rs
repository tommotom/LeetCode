impl Solution {
    pub fn find_redundant_connection(edges: Vec<Vec<i32>>) -> Vec<i32> {
        let n = edges.len();
        let mut ids = Vec::new();
        for i in 0..n+1 {
            ids.push(i as i32);
        }

        fn find(mut u: i32, ids: &mut Vec<i32>) -> i32 {
            if u != ids[u as usize] {
                ids[u as usize] = find(ids[u as usize], ids);
            }
            ids[u as usize]
        }

        fn union(mut u: i32, mut v: i32, ids: &mut Vec<i32>) {
            u = find(u, ids);
            v = find(v, ids);
            ids[u as usize] = v;
        }

        for i in 0..n {
            let u = edges[i][0] - 1;
            let v = edges[i][1] - 1;
            if find(u, &mut ids) == find(v, &mut ids) {
                return edges[i].clone();
            }
            union(u, v, &mut ids);
        }

        edges[0].clone()
    }
}

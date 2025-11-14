impl Solution {
    pub fn range_add_queries(n: i32, mut queries: Vec<Vec<i32>>) -> Vec<Vec<i32>> {
        let mut queries: Vec<Vec<usize>> = queries.iter().map(|q| vec![q[0] as usize, q[1] as usize, q[2] as usize, q[3] as usize]).collect();
        let n = n as usize;

        let mut cum = vec![vec![0; n]; n];
        for query in queries {
            for r in query[0]..=query[2] {
                cum[r][query[1]] += 1;
                if query[3] + 1 < n {
                    cum[r][(n-1).min(query[3]+1)] -= 1;
                }
            }
        }

        let mut ans = vec![vec![0; n]; n];
        for i in 0..n {
            let mut cur = 0;
            for j in 0..n {
                cur += cum[i][j];
                ans[i][j] = cur;
            }
        }
        ans
    }
}

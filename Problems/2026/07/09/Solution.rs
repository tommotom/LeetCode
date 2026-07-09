impl Solution {
    pub fn path_existence_queries(n: i32, nums: Vec<i32>, max_diff: i32, queries: Vec<Vec<i32>>) -> Vec<bool> {
        let n = n as usize;
        let mut group = vec![0];
        let mut g = 0;
        for i in 1..n {
            if nums[i] - nums[i-1] > max_diff {
                g += 1;
            }
            group.push(g);
        }
        queries.iter().map(|q| group[q[0] as usize] == group[q[1] as usize]).collect()
    }
}

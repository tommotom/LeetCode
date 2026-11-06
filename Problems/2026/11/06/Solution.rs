use std::collections::{VecDeque, HashMap};

impl Solution {
    pub fn count_servers(n: i32, mut logs: Vec<Vec<i32>>, x: i32, queries: Vec<i32>) -> Vec<i32> {
        logs.sort_by(|a, b| a[1].cmp(&b[1]));
        let mut queries: Vec<(usize, i32)> = queries.iter().enumerate().map(|(i, &q)| (i, q)).collect();
        queries.sort_by(|a, b| a.1.cmp(&b.1));
        let mut ans = vec![0; queries.len()];
        let mut deq: VecDeque<(i32, i32)> = VecDeque::new();
        let mut counter = HashMap::new();
        let mut j = 0;
        for (i, q) in queries {
            let start = q - x;
            while j < logs.len() && logs[j][1] <= q {
                let server = logs[j][0];
                deq.push_back((logs[j][1], logs[j][0]));
                *counter.entry(server).or_insert(0) += 1;
                j += 1;
            }
            while deq.len() > 0 && deq[0].0 < start {
                let server = deq.pop_front().unwrap().1;
                *counter.entry(server).or_insert(0) -= 1;
                if *counter.get(&server).unwrap() == 0 {
                    counter.remove(&server);
                }
            }
            ans[i] = n - counter.len() as i32;
        }
        ans
    }
}

use std::collections::HashMap;
use std::collections::VecDeque;

impl Solution {
    pub fn min_jumps(arr: Vec<i32>) -> i32 {
        let mut val_to_i: HashMap<i32, Vec<usize>> = HashMap::new();
        let n = arr.len();
        for i in 0..n {
            val_to_i.entry(arr[i]).or_insert(Vec::new()).push(i);
        }
        let mut dp = vec![n as i32; n];
        dp[0] = 0;

        let mut q: VecDeque<(usize, i32)> = VecDeque::new();
        q.push_back((0, 0));
        while q.len() > 0 {
            let (i, jumps) = q.pop_front().unwrap();
            if dp[i] > jumps {
                continue;
            }
            if i > 0 && dp[i-1] > jumps + 1 {
                dp[i-1] = jumps + 1;
                q.push_back((i-1, jumps + 1));
            }
            if i + 1 < n && dp[i+1] > jumps + 1 {
                dp[i+1] = jumps + 1;
                q.push_back((i+1, jumps + 1));
            }
            for j in val_to_i.entry(arr[i]).or_default() {
                if i == *j {
                    continue;
                }
                if dp[*j] > jumps + 1 {
                    dp[*j] = jumps + 1;
                    q.push_back((*j, jumps + 1));
                }
            }
            val_to_i.remove(&arr[i]);
        }
        dp[n-1]
    }
}

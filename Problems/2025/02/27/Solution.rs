use std::collections::HashMap;

impl Solution {
    pub fn len_longest_fib_subseq(arr: Vec<i32>) -> i32 {
        let n = arr.len();
        let mut len = Vec::new();
        let mut val_to_idx = HashMap::new();
        for i in 0..n {
            len.push(vec![0; n]);
            val_to_idx.insert(arr[i], i);
        }

        let mut ans = 0;
        for i in 1..n {
            for j in 0..i {
                let diff = arr[i] - arr[j];
                if let Some(k) = val_to_idx.get(&diff) {
                    len[j][i] = if diff < arr[j] {len[*k][j] + 1} else {2};
                } else {
                    len[j][i] = 2;
                }
                ans = ans.max(len[j][i]);
            }
        }
        if ans > 2 {ans} else {0}
    }
}

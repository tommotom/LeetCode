use std::collections::HashMap;

impl Solution {
    pub fn min_cost(basket1: Vec<i32>, basket2: Vec<i32>) -> i64 {
        let mut counter = HashMap::new();
        let mut min = i32::MAX;
        for &b in &basket1 {
            *counter.entry(b).or_insert(0) += 1;
            min = min.min(b);
        }
        for &b in &basket2 {
            *counter.entry(b).or_insert(0) -= 1;
            min = min.min(b);
        }

        let mut merge = Vec::new();
        for (&k, &v) in counter.iter() {
            if v % 2 == 1 {
                return -1;
            }
            for _ in 0..((v as i32).abs()/2) {
                merge.push(k);
            }
        }
        merge.sort();
        merge.iter().take(merge.len()/2).map(|&x| i64::from(x.min(min*2))).sum()
    }
}

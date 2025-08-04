use std::collections::HashMap;

impl Solution {
    pub fn total_fruit(fruits: Vec<i32>) -> i32 {
        let mut counter = HashMap::new();
        let mut l = 0;
        let mut ans = 0;
        for r in 0..fruits.len() {
            *counter.entry(fruits[r]).or_insert(0) += 1;
            while counter.len() > 2 {
                *counter.entry(fruits[l]).or_insert(0) -= 1;
                if *counter.get(&fruits[l]).unwrap() == 0 {
                    counter.remove(&fruits[l]);
                }
                l += 1;
            }
            ans = ans.max(r - l + 1);
        }
        ans as i32
    }
}

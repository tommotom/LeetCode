use std::collections::HashMap;

impl Solution {
    pub fn num_rabbits(answers: Vec<i32>) -> i32 {
        let mut ans = 0;
        let mut counter = HashMap::new();
        for a in answers {
            *counter.entry(a).or_insert(0) += 1;
            if *counter.get(&a).unwrap() == a + 1 {
                ans += a + 1;
                counter.remove(&a);
            }
        }
        if counter.len() > 0 { counter.into_keys().map(|a| a + 1).reduce(|a, b| a + b).unwrap() + ans } else { ans }
    }
}

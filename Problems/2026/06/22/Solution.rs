use std::collections::HashMap;

impl Solution {
    pub fn max_number_of_balloons(text: String) -> i32 {
        let mut counter: HashMap<char, i32> = HashMap::new();
        for c in text.chars() {
            *counter.entry(c).or_insert(0) += 1;
        }
        *counter.get(&'b').unwrap_or(&0)
        .min(counter.get(&'a').unwrap_or(&0))
        .min(&(counter.get(&'l').unwrap_or(&0) / 2))
        .min(&(counter.get(&'o').unwrap_or(&0) / 2))
        .min(counter.get(&'n').unwrap_or(&0))
    }
}

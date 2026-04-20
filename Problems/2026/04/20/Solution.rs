use std::collections::HashMap;

impl Solution {
    pub fn max_distance(colors: Vec<i32>) -> i32 {
        let mut ans = 0;
        let mut seen_at = HashMap::new();
        for i in 0..colors.len() {
            if !seen_at.contains_key(&colors[i]) {
                seen_at.insert(colors[i], i);
            }
            for key in seen_at.keys() {
                if *key == colors[i] {
                    continue;
                }
                ans = ans.max(i - seen_at.get(key).unwrap());
            }
        }
        ans as i32
    }
}

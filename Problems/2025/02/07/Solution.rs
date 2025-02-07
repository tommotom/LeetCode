use std::collections::HashMap;

impl Solution {
    pub fn query_results(limit: i32, queries: Vec<Vec<i32>>) -> Vec<i32> {
        let mut color = HashMap::new();
        let mut color_count = HashMap::new();
        let mut ans = Vec::new();
        for q in queries {
            let x = q[0];
            let y = q[1];
            if let Some(old_color) = color.get(&x) {
                if let Some(v) = color_count.get_mut(old_color) {
                    *v -= 1;
                    if *v == 0 {
                        color_count.remove(old_color);
                    }
                }
            }
            color.insert(x, y);
            *color_count.entry(y).or_insert(0) += 1;
            ans.push(color_count.len() as i32);
        }
        ans
    }
}

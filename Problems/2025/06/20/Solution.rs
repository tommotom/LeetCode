use std::collections::HashMap;

impl Solution {
    pub fn max_distance(s: String, k: i32) -> i32 {
        let dir = HashMap::from([
            ('N', (0, 1)),
            ('S', (0, -1)),
            ('E', (1, 0)),
            ('W', (-1, 0)),
        ]);
        let mut ans = 0;
        [('N', 'E', 'S', 'W'), ('N', 'W', 'S', 'E'), ('S', 'W', 'N', 'E'), ('S', 'E', 'N', 'W')].iter().for_each(|replace| {
            let mut x: i32 = 0; let mut y: i32 = 0; let mut replaced = 0;
            for c in s.chars() {
                if replaced < k && c == replace.0 {
                    replaced += 1;
                    y += dir.get(&replace.2).unwrap().0;
                    x += dir.get(&replace.2).unwrap().1;
                } else if replaced < k && c == replace.1 {
                    replaced += 1;
                    y += dir.get(&replace.3).unwrap().0;
                    x += dir.get(&replace.3).unwrap().1;
                } else {
                    y += dir.get(&c).unwrap().0;
                    x += dir.get(&c).unwrap().1;
                }
                ans = ans.max(x.abs() + y.abs());
            }
        });
        ans
    }
}

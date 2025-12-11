use std::collections::HashMap;

impl Solution {
    pub fn count_covered_buildings(n: i32, buildings: Vec<Vec<i32>>) -> i32 {
        let mut l: HashMap<i32, i32> = HashMap::new();
        let mut r: HashMap<i32, i32> = HashMap::new();
        let mut u: HashMap<i32, i32> = HashMap::new();
        let mut d: HashMap<i32, i32> = HashMap::new();
        for b in &buildings {
            let (x, y) = (b[0], b[1]);
            l.entry(y).and_modify(|v| *v = (*v).min(x)).or_insert(x);
            r.entry(y).and_modify(|v| *v = (*v).max(x)).or_insert(x);
            u.entry(x).and_modify(|v| *v = (*v).max(y)).or_insert(y);
            d.entry(x).and_modify(|v| *v = (*v).min(y)).or_insert(y);
        }

        let mut ans = 0;
        for b in &buildings {
            let (x, y) = (b[0], b[1]);
            if l[&y] == x || r[&y] == x || u[&x] == y || d[&x] == y {
                continue;
            }
            ans += 1;
        }
        ans
    }
}

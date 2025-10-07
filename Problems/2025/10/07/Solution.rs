use std::collections::HashMap;

impl Solution {
    pub fn avoid_flood(rains: Vec<i32>) -> Vec<i32> {
        let mut ans = vec![-1; rains.len()];
        let mut rained_at = HashMap::new();
        let mut dry_at = Vec::new();
        for i in 0..rains.len() {
            if rains[i] == 0 {
                dry_at.push(i);
                continue;
            }
            let r = rains[i];
            if rained_at.contains_key(&r) {
                let mut is_valid = false;
                let j = rained_at.get(&r).unwrap();
                for d in 0..dry_at.len() {
                    if (*j as usize) < dry_at[d] {
                        ans[dry_at[d]] = r;
                        dry_at.remove(d);
                        is_valid = true;
                        break;
                    }
                }
                if !is_valid {
                    return Vec::new();
                }
            }
            rained_at.insert(r, i);
        }
        for i in 0..dry_at.len() {
            ans[dry_at[i]] = 1;
        }
        ans
    }
}

use std::collections::HashSet;

impl Solution {
    pub fn maximize_square_area(m: i32, n: i32, mut h_fences: Vec<i32>, mut v_fences: Vec<i32>) -> i32 {
        h_fences.sort();
        v_fences.sort();
        let (m, n) = (m as i64, n as i64);
        let mut hs = HashSet::new();
        hs.insert(m - 1);
        for e in 0..h_fences.len() {
            hs.insert(h_fences[e] as i64 - 1);
            hs.insert(m - h_fences[e] as i64);
            for s in 0..e {
                hs.insert(h_fences[e] as i64 - h_fences[s] as i64);
            }
        }
        if hs.contains(&(n-1)) {
            return (((n-1) * (n-1)) % 1000000007) as i32;
        }
        let mut ans = -1;
        for e in 0..v_fences.len() {
            let a = v_fences[e] as i64 - 1;
            if hs.contains(&a) {
                ans = ans.max(a * a);
            }
            let b = n - v_fences[e] as i64;
            if hs.contains(&b) {
                ans = ans.max(b * b);
            }
            for s in 0..e {
                let c = v_fences[e] as i64 - v_fences[s] as i64;
                if hs.contains(&c) {
                    ans = ans.max(c * c);
                }
            }
        }
        (ans % 1000000007) as i32
    }
}

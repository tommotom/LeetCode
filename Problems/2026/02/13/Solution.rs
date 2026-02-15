use std::collections::HashMap;

impl Solution {
    pub fn longest_balanced(s: String) -> i32 {
        let (mut m, mut k, mut c, mut f) = (vec![HashMap::from([(0,-1)]);4], [0;3], [0;3], 0);
        s.bytes().enumerate().map(|(i, b)| {
            f = 1 + f * (i > 0 && b == s.as_bytes()[i-1]) as i32;
            let (i, x) = (i as i32, (b - 97) as usize); c[x] += 1;
            (0..3).map(|e| if x == e { m[e] = HashMap::from([(0, i)]); k[e] = 0; 0 } else {
                k[e] += ((x + 1) % 3 == e) as i32 * 2 - 1; i - *m[e].entry(k[e]).or_insert(i)
            }).max().unwrap().max(i - *m[3].entry(((c[1]-c[0])<<16)+c[2]-c[0]).or_insert(i)).max(f)
        }).max().unwrap_or(0)
    }
}

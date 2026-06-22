impl Solution {
    pub fn max_ice_cream(c: Vec<i32>, mut k: i32) -> i32 {
        let m = *c.iter().max().unwrap();
        let mut s = vec![0; m as usize + 1];
        for x in c {
            s[x as usize] += 1
        }
        (1..=m).map(|i| {
            let r = s[i as usize].min(k / i);
            k -= r * i;
            r
        }).sum()
    }
}

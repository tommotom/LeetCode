use std::collections::HashSet;

impl Solution {
    pub fn num_tile_possibilities(tiles: String) -> i32 {
        let mut counter = vec![0; 26];
        for c in tiles.chars() {
            counter[c.to_ascii_lowercase() as u8 as usize - 97] += 1;
        }
        let mut seq: HashSet<i64> = HashSet::new();
        Self::helper(tiles.len(), &mut seq, &mut counter, 0);
        seq.len() as i32
    }

    fn helper(n: usize, seq: &mut HashSet<i64>, counter: &mut Vec<i32>, mut num: i64) {
        if n == 0 {
            return;
        }
        for i in 0..26 {
            if counter[i] > 0 {
                counter[i] -= 1;
                num *= 26;
                num += i as i64 + 1;
                seq.insert(num);
                Self::helper(n-1, seq, counter, num);
                num -= i as i64 + 1;
                num /= 26;
                counter[i] += 1;
            }
        }
    }
}

impl Solution {
    pub fn successful_pairs(spells: Vec<i32>, mut potions: Vec<i32>, success: i64) -> Vec<i32> {
        potions.sort();
        let spells: Vec<i64> = spells.iter().map(|s| *s as i64).collect();
        let potions: Vec<i64> = potions.iter().map(|p| *p as i64).collect();
        let mut pairs = Vec::new();
        for s in spells {
            let (mut l, mut r) = (0, potions.len());
            while l < r {
                let m = l + (r - l) / 2;
                if s * potions[m] < success {
                    l = m + 1;
                } else {
                    r = m;
                }
            }
            pairs.push((potions.len() - l) as i32);
        }
        pairs
    }
}

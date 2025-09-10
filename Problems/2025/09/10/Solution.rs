use std::collections::{HashSet, HashMap};

impl Solution {
    pub fn minimum_teachings(n: i32, languages: Vec<Vec<i32>>, friendships: Vec<Vec<i32>>) -> i32 {
        let mut cncon = HashSet::new();
        for friendship in friendships {
            let mut mp = HashSet::new();
            let mut conm = false;
            for &lan in &languages[friendship[0] as usize - 1] {
                mp.insert(lan);
            }
            for &lan in &languages[friendship[1] as usize - 1] {
                if mp.contains(&lan) {
                    conm = true;
                    break;
                }
            }

            if !conm {
                cncon.insert(friendship[0] - 1);
                cncon.insert(friendship[1] - 1);
            }
        }

        let mut max_cnt = 0;
        let mut cnt = HashMap::new();
        for &person in &cncon {
            for &lan in &languages[person as usize] {
                *cnt.entry(lan).or_insert(0) += 1;
                max_cnt = max_cnt.max(*cnt.get(&lan).unwrap());
            }
        }

        cncon.len() as i32 - max_cnt
    }
}

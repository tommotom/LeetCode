use std::collections::{HashMap, HashSet};

impl Solution {
    pub fn spellchecker(wordlist: Vec<String>, queries: Vec<String>) -> Vec<String> {
        fn devowel(s: &str) -> String {
            s.to_ascii_lowercase()
                .chars()
                .map(|c| match c {
                    'a' | 'e' | 'i' | 'o' | 'u' => '*',
                    _ => c,
                })
                .collect()
        }

        let perfect: HashSet<String> = wordlist.iter().cloned().collect();
        let mut cap: HashMap<String, String> = HashMap::new();
        let mut vow: HashMap<String, String> = HashMap::new();

        for w in &wordlist {
            let lower = w.to_ascii_lowercase();
            cap.entry(lower.clone()).or_insert_with(|| w.clone());
            let dv = devowel(&lower);
            vow.entry(dv).or_insert_with(|| w.clone());
        }

        queries
            .into_iter()
            .map(|q| {
                if perfect.contains(&q) {
                    return q;
                }
                let lower = q.to_ascii_lowercase();
                if let Some(ans) = cap.get(&lower) {
                    return ans.clone();
                }
                let dv = devowel(&lower);
                if let Some(ans) = vow.get(&dv) {
                    return ans.clone();
                }
                String::new()
            })
            .collect()
    }
}

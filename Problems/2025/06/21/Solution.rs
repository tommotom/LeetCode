use std::collections::HashMap;

impl Solution {
    pub fn minimum_deletions(word: String, k: i32) -> i32 {
        let mut freq = HashMap::new();
        for c in word.chars() {
            *freq.entry(c).or_insert(0) += 1;
        }
        let mut freq: Vec<i32> = freq.values().cloned().collect();
        freq.sort();
        let n = word.len() as i32;
        let mut ans = n; let mut deleted = 0;
        for l in 0..freq.len() {
            let mut sum = 0;
            for r in (l+1)..freq.len() {
                sum += (freq[r] - freq[l] - k).max(0);
            }
            ans = ans.min(deleted + sum);
            deleted += freq[l];
        }
        ans
    }
}

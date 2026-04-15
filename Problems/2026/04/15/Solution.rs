impl Solution {
    pub fn closest_target(words: Vec<String>, target: String, start_index: i32) -> i32 {
        let n = words.len();
        let mut targets = Vec::new();
        for i in 0..n {
            if words[i] == target {
                targets.push(i as i32);
            }
        }
        if targets.len() == 0 {
            return -1;
        }
        let mut ans = i32::MAX;
        for i in targets {
            ans = ans.min((n as i32 + i - start_index) % n as i32);
            ans = ans.min((n as i32 + start_index - i) % n as i32);
        }
        ans
    }
}

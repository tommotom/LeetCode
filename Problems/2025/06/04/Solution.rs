impl Solution {
    pub fn answer_string(word: String, num_friends: i32) -> String {
        let num_friends = num_friends as usize;
        if num_friends == 1 { return word; }
        let max_substr_len = word.len() - (num_friends - 1);
        let mut max_so_far: Option<&str> = None;
        for b in 0..word.len() {
            let end_idx = word.len().min(b + max_substr_len);
            let candidate = Some(&word[b..end_idx]);
            max_so_far = max_so_far.max(candidate);
        }
        max_so_far.unwrap().to_string()
    }
}

impl Solution {
    pub fn max_depth_after_split(seq: String) -> Vec<i32> {
        seq.chars()
        .enumerate()
        .map(|(i, c)| {
            (i as i32 & 1) ^ if c == '(' { 1 } else { 0 }
        })
        .collect()
    }
}

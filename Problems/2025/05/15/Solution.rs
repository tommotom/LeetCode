impl Solution {
    pub fn get_longest_subsequence(words: Vec<String>, groups: Vec<i32>) -> Vec<String> {
        let n = words.len();
        let mut ans = Vec::new();
        let mut last = -1;
        for i in 0..n {
            if (last != groups[i]) {
                last = groups[i];
                ans.push(words[i].clone());
            }
        }
        ans
    }
}

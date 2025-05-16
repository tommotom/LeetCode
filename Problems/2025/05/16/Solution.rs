impl Solution {
    pub fn get_words_in_longest_subsequence(words: Vec<String>, groups: Vec<i32>) -> Vec<String> {

        fn is_valid_pair(a: Vec<char>, b: Vec<char>) -> bool {
            if a.len() != b.len() {
                return false;
            }
            let mut distance = 0;
            for i in 0..a.len() {
                if a[i] != b[i] {
                    distance += 1;
                }
            }
            distance == 1
        }

        let n = words.len();
        let mut dp = vec![1; n];
        let mut prev = vec![-1; n];
        for i in 1..n {
            for j in 0..i {
                if groups[i] != groups[j] && is_valid_pair(words[i].chars().collect(), words[j].chars().collect()) {
                    if dp[i] < dp[j] + 1 {
                        dp[i] = dp[j] + 1;
                        prev[i] = j as i32;
                    }
                }
            }
        }
        let max = dp.clone().into_iter().reduce(|a, b| a.max(b)).unwrap();
        let mut ans = Vec::new();
        for i in (0..n).rev() {
            if dp[i] == max {
                let mut cur = i as i32;
                while cur >= 0 {
                    ans.push(words[cur as usize].clone());
                    cur = prev[cur as usize];
                }
                break;
            }
        }
        ans.into_iter().rev().collect()
    }
}

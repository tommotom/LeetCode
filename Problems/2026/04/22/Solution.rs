impl Solution {
    pub fn two_edit_words(queries: Vec<String>, dictionary: Vec<String>) -> Vec<String> {
        fn distance(a: Vec<char>, b: Vec<char>) -> i32 {
            let mut ret = 0;
            for i in 0..a.len() {
                if a[i] != b[i] {
                    ret += 1;
                }
            }
            ret
        }

        let mut ans = Vec::new();
        for i in 0..queries.len() {
            for j in 0..dictionary.len() {
                if distance(queries[i].chars().collect(), dictionary[j].chars().collect()) <= 2 {
                    ans.push(queries[i].clone());
                    break;
                }
            }
        }
        ans
    }
}

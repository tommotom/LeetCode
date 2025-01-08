impl Solution {
    fn is_substring(a: String, b: String) -> bool {
        if a.len() == b.len() {
            return false;
        }
        for i in 0..b.len()-a.len()+1 {
            let mut is_valid = true;
            for j in 0..a.len() {
                if a.chars().nth(j).unwrap() != b.chars().nth(i+j).unwrap() {
                    is_valid = false;
                    break;
                }
            }
            if is_valid {
                return true;
            }
        }
        false
    }

    pub fn string_matching(mut words: Vec<String>) -> Vec<String> {
        words.sort_by(|a, b| a.len().cmp(&b.len()));
        let mut ans = Vec::new();
        for i in 0..words.len()-1 {
            let mut is_valid = false;
            for j in i+1..words.len() {
                if Self::is_substring(words[i].clone(), words[j].clone()) {
                    is_valid = true;
                    break;
                }
            }
            if is_valid {
                ans.push(words[i].clone())
            }
        }
        ans
    }
}

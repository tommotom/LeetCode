impl Solution {
    fn is_prefix_and_suffix(a: String, b: String) -> bool {
        let m = a.len();
        let n = b.len();
        if (m > n) {
            return false;
        }
        for i in 0..a.len() {
            if a.chars().nth(i).unwrap() != b.chars().nth(i).unwrap() {
                return false;
            }
            if a.chars().nth(m-i-1).unwrap() != b.chars().nth(n-i-1).unwrap() {
                return false;
            }
        }
        true
    }

    pub fn count_prefix_suffix_pairs(mut words: Vec<String>) -> i32 {
        let mut ans = 0;
        for i in 0..words.len()-1 {
            for j in i+1..words.len() {
                if Self::is_prefix_and_suffix(words[i].clone(), words[j].clone()) {
                    ans += 1;
                }
            }
        }
        ans
    }
}

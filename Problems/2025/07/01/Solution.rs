impl Solution {
    pub fn possible_string_count(word: String) -> i32 {
        let mut ans = 1;
        let word: Vec<char> = word.chars().collect();
        let mut count = 1;
        for i in 1..word.len() {
            if word[i-1] != word[i] {
                ans += count - 1;
                count = 1;
            } else {
                count += 1;
            }
        }
        ans + (count - 1)
    }
}

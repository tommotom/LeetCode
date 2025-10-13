impl Solution {
    pub fn remove_anagrams(words: Vec<String>) -> Vec<String> {
        fn to_index(c: char) -> usize {
            (c as u8 - 'a' as u8) as usize
        }

        fn count(word: &String) -> Vec<i32> {
            let mut counter = vec![0; 26];
            for c in word.chars() {
                counter[to_index(c)] += 1;
            }
            counter
        }

        fn is_anagram(a: &String, b: &String) -> bool {
            let (aa, bb) = (count(a), count(b));
            for i in 0..26 {
                if aa[i] != bb[i] {
                    return false;
                }
            }
            true
        }

        let mut ans = Vec::new();
        ans.push(words[0].clone());
        let mut i = 0;
        for j in 1..words.len() {
            if !is_anagram(&words[i], &words[j]) {
                ans.push(words[j].clone());
                i = j;
            }
        }
        ans
    }
}

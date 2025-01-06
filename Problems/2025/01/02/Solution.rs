impl Solution {
    fn is_vowel(c: char) -> bool {
        return c == 'a' || c == 'i' || c == 'u' || c == 'e' || c == 'o';
    }

    fn starts_with_vowel(word: String) -> bool {
        return Self::is_vowel(word.chars().nth(0).unwrap());
    }

    fn ends_with_vowel(word: String) -> bool{
        let n = word.len();
        return Self::is_vowel(word.chars().nth(n-1).unwrap());
    }

    fn is_valid(word: String) -> bool {
        return Self::starts_with_vowel(word.clone()) && Self::ends_with_vowel(word.clone());
    }

    pub fn vowel_strings(words: Vec<String>, queries: Vec<Vec<i32>>) -> Vec<i32> {
        let mut arr = Vec::new();
        arr.push(0);
        let mut count = 0;

        for string in words {
            if Self::is_valid(string) {
                count += 1;
            }
            arr.push(count);
        }

        let mut ans = Vec::new();
        for query in queries {
            let l = query[0];
            let r = query[1];
            ans.push(arr[(r + 1) as usize] - arr[l as usize]);
        }
        ans
    }
}

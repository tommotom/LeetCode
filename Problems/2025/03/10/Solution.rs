use std::collections::HashMap;

impl Solution {
    pub fn count_of_substrings(word: String, k: i32) -> i64 {
        fn to_index(c: char) -> usize {
            match c {
                'a' => 0,
                'i' => 1,
                'u' => 2,
                'e' => 3,
                'o' => 4,
                _ => 5
            }
        }

        fn has_every_vowel(counter: &Vec<Vec<i32>>, i: usize, j: usize) -> bool {
            for index in 0..5 {
                if counter[i][index] - counter[j][index] == 0 {
                    return false;
                }
            }
            true
        }

        let mut counter = Vec::new();
        counter.push(vec![0; 6]);
        let mut l = 0;
        let mut r = 0;
        let mut ans: i64 = 0;
        for (i, w) in word.chars().enumerate() {
            counter.push(counter[i].to_vec());
            counter[i+1][to_index(w)] += 1;
            while has_every_vowel(&counter, i+1, l) && counter[i+1][5] - counter[l][5] > k {
                l += 1;
            }
            while has_every_vowel(&counter, i+1, r) && counter[i+1][5] - counter[r][5] >= k {
                r += 1;
            }
            ans += (r - l) as i64;
        }
        ans
    }
}

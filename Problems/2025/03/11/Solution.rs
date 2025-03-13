impl Solution {
    pub fn number_of_substrings(s: String) -> i32 {
        fn to_vec(c: char) -> usize {
            if c == 'a' {
                return 0;
            } else if c == 'b' {
                return 1;
            }
            2
        }

        fn has_all_chars(counter: &Vec<Vec<i32>>, l: usize, r: usize) -> bool {
            counter[r+1][0] - counter[l][0] > 0 && counter[r+1][1] - counter[l][1] > 0 && counter[r+1][2] - counter[l][2] > 0
        }

        let mut counter = Vec::new();
        counter.push(vec![0; 3]);
        let mut l = 0;
        let mut ans = 0;
        for (r, w) in s.chars().enumerate() {
            counter.push(counter[r].to_vec());
            counter[r+1][to_vec(w)] += 1;
            while has_all_chars(&counter, l, r) {
                l += 1;
            }
            ans += l as i32;
        }
        ans
    }
}

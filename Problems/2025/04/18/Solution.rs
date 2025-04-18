impl Solution {
    pub fn count_and_say(n: i32) -> String {
        fn next(chars: Vec<char>) -> Vec<char> {
            let mut arr = Vec::new();
            let mut count = 1;
            let mut cur = chars[0];
            for i in 1..chars.len() {
                if cur == chars[i] {
                    count += 1;
                } else {
                    arr.push(char::from_digit(count as u32, 10).unwrap());
                    arr.push(cur);
                    cur = chars[i];
                    count = 1;
                }
            }
            arr.push(char::from_digit(count as u32, 10).unwrap());
            arr.push(cur);
            arr
        }

        let mut ans = vec!['1'];

        for i in 1..n {
            ans = next(ans);
        }

        ans.iter().collect()
    }
}

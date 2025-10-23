impl Solution {
    pub fn has_same_digits(s: String) -> bool {
        fn helper(u8s: Vec<u8>) -> Vec<u8> {
            if u8s.len() == 2 {
                return u8s;
            }
            let mut arr = Vec::new();
            for i in 1..u8s.len() {
                arr.push((u8s[i-1] + u8s[i]) % 10);
            }
            helper(arr)
        }
        let u8s: Vec<u8> = helper(s.chars().map(|c| c as u8).collect());
        u8s[0] == u8s[1]
    }
}

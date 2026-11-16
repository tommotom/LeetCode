impl Solution {
    pub fn digit_sum(s: String, k: i32) -> String {
        let k = k as usize;
        if s.len() <= k {
            return s;
        }
        let mut chars: Vec<char> = s.chars().collect();
        let mut arr = Vec::new();
        let mut i = 0;
        while i < s.len() {
            let mut sum = 0;
            for j in i..(i+k).min(s.len()) {
                sum += chars[j].to_digit(10).unwrap() as i32;
            }
            arr.push(sum.to_string());
            i += k;
        }
        Self::digit_sum(arr.concat(), k as i32)
    }
}

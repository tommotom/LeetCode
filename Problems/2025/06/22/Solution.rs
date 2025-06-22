impl Solution {
    pub fn divide_string(s: String, k: i32, fill: char) -> Vec<String> {
        let k = k as usize;
        let mut ans = Vec::new();
        let mut arr = Vec::new();
        for c in s.chars() {
            arr.push(c);
            if arr.len() == k {
                ans.push(arr.iter().collect());
                arr = Vec::new();
            }
        }
        while arr.len() > 0 && arr.len() < k {
            arr.push(fill);
        }
        if arr.len() > 0 {
            ans.push(arr.iter().collect());
        }
        ans
    }
}

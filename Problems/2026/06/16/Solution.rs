impl Solution {
    pub fn process_str(s: String) -> String {
        let mut arr = Vec::new();
        for c in s.chars() {
            if c == '*' {
                if arr.len() > 0 {
                    arr.pop();
                }
            } else if c == '#' {
                arr.extend(arr.clone().into_iter());
            } else if c == '%' {
                arr = arr.into_iter().rev().collect();
            } else {
                arr.push(c);
            }
        }
        arr.into_iter().collect()
    }
}

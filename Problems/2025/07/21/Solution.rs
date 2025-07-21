impl Solution {
    pub fn make_fancy_string(s: String) -> String {
        let mut last = "";
        let mut last2 = "";
        let mut arr = Vec::new();
        for c in s.chars() {
            let c = c.to_string();
            let n = arr.len();
            if n > 1 && arr[n-2] == arr[n-1] && arr[n-1] == c {
                continue;
            }
            arr.push(c);
        }
        arr.join("")
    }
}

impl Solution {
    pub fn shortest_beautiful_substring(s: String, k: i32) -> String {
        let mut count = vec![0; s.len()];
        let s: Vec<char> = s.chars().collect();
        for i in 0..s.len() {
            if i > 0 {
                count[i] = count[i-1];
            }
            if s[i] == '1' {
                count[i] += 1
            }
        }
        let k = k as usize;
        for len in k..=s.len() {
            let mut c = 0;
            for i in 0..(len-1) {
                if s[i] == '1' {
                    c += 1;
                }
            }
            let mut ret: Option<String> = None;
            for i in (len-1)..s.len() {
                if s[i] == '1' {
                    c += 1;
                }
                if c == k {
                    let can: String = s.iter().skip(i-len+1).take(len).collect();
                    ret = Some(match ret {
                        Some(st) => st.min(can),
                        None => can
                    })
                }
                if s[i-len+1] == '1' {
                    c -= 1;
                }
            }
            if let Some(ans) = ret {
                return ans;
            }
        }
        "".to_string()
    }
}

use std::collections::HashSet;

impl Solution {
    pub fn validate_coupons(code: Vec<String>, business_line: Vec<String>, is_active: Vec<bool>) -> Vec<String> {
        fn is_alphanumeric(c: char) -> bool {
            let u = c as u8;
            (('0' as u8) <= u && u <= ('9' as u8)) || (('A' as u8) <= u && u <= ('Z' as u8)) || (('a' as u8) <= u && u <= ('z' as u8)) || c == '_'
        }

        fn is_valid(code: String, business_line: String, is_active: bool) -> bool {
            if code.len() == 0 {
                return false;
            }
            if code.chars().any(|c| !is_alphanumeric(c)) {
                return false;
            }
            let set: HashSet<String> = ["electronics".to_string(), "grocery".to_string(), "pharmacy".to_string(), "restaurant".to_string()].into_iter().collect::<HashSet<_>>();
            if !set.contains(&business_line) {
                return false;
            }
            is_active
        }

        let mut filtered = Vec::new();
        for i in 0..code.len() {
            if is_valid(code[i].clone(), business_line[i].clone(), is_active[i]) {
                filtered.push((code[i].clone(), business_line[i].clone()));
            }
        }

        filtered.sort_by(|a, b| if a.1 != b.1 {a.1.cmp(&b.1)} else {a.0.cmp(&b.0)});

        filtered.iter().map(|a| a.0.clone()).collect()
    }
}

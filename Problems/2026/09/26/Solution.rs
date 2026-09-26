use std::collections::HashMap;

impl Solution {
    pub fn evaluate(s: String, knowledge: Vec<Vec<String>>) -> String {
        let mut map: HashMap<String, String> = HashMap::new();
        for k in knowledge {
            map.insert(k[0].clone(), k[1].clone());
        }

        let mut ans = Vec::new();
        let mut in_bracket = false;
        let mut key = Vec::new();
        for c in s.chars() {
            if c == '(' {
                in_bracket = true;
                key = Vec::new();
                continue;
            }
            if c == ')' {
                let k = key.iter().cloned().collect::<String>();
                if map.contains_key(&k) {
                    ans.extend(map.get(&k).unwrap().chars());
                } else {
                    ans.push('?');
                }
                in_bracket = false;
                continue;
            }
            if in_bracket {
                key.push(c);
            } else {
                ans.push(c);
            }
        }

        ans.into_iter().collect()
    }
}

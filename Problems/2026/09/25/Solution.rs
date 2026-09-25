use std::collections::BTreeSet;

impl Solution {
    pub fn brace_expansion_ii(expression: String) -> Vec<String> {
        let chars: Vec<char> = expression.chars().collect();
        let mut idx = 0;
        let n = chars.len();

        fn is_letter(c: char) -> bool {
            c >= 'a' && c <= 'z'
        }

        fn item_impl(idx: &mut usize, chars: &[char]) -> BTreeSet<String> {
            let mut ret = BTreeSet::new();
            if chars[*idx] == '{' {
                *idx += 1;
                ret = expr_impl(idx, chars);
            } else {
                ret.insert(chars[*idx].to_string());
            }
            *idx += 1;
            ret
        }

        fn term_impl(idx: &mut usize, chars: &[char]) -> BTreeSet<String> {
            let mut ret = BTreeSet::new();
            ret.insert(String::new());
            while *idx < chars.len() && (chars[*idx] == '{' || is_letter(chars[*idx])) {
                let sub = item_impl(idx, chars);
                let mut tmp = BTreeSet::new();
                for left in &ret {
                    for right in &sub {
                        tmp.insert(format!("{}{}", left, right));
                    }
                }
                ret = tmp;
            }
            ret
        }

        fn expr_impl(idx: &mut usize, chars: &[char]) -> BTreeSet<String> {
            let mut ret = BTreeSet::new();
            loop {
                for item in term_impl(idx, chars) {
                    ret.insert(item);
                }
                if *idx < chars.len() && chars[*idx] == ',' {
                    *idx += 1;
                    continue;
                } else {
                    break;
                }
            }
            ret
        }

        let result = expr_impl(&mut idx, &chars);
        result.into_iter().collect()
    }
}

use std::collections::HashMap;

impl Solution {
  pub fn maximum_length_substring(s: String) -> i32 {
    let mut res = 0;
    let n = s.len();
    for i in 0..n-1 {
      for j in i+1..n+1 {
        let substr: String = s[i..j].to_string();
        let mut hm:HashMap<char,i32> = HashMap::new();
        let mut safe = true;
        for c in substr.chars() {
          *hm.entry(c).or_insert(0)+=1;
          if *hm.entry(c).or_insert(0) > 2 {
            safe = false;
            break;
          }
        }
        if safe {
          res = res.max((j-i) as i32);
        }
      }
    }
    res
  }
}

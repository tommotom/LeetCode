impl Solution {
        pub fn valid_sequence(w: String, t: String) -> Vec<i32> {
        let (mut r, mut l) = (vec![], vec![0; t.len()]);let mut j=t.len()-1;
        for i in (0..w.len()).rev() {
            if w.as_bytes()[i] == t.as_bytes()[j] { l[j] = i+1; if j<1 {break};j -= 1 } }
        j = 0; let mut skip = true;
        for i in 0..w.len() {
            if w.as_bytes()[i] == t.as_bytes()[j] || skip && (j+1==t.len()||i+1 < l[j+1]) {
                if w.as_bytes()[i] != t.as_bytes()[j] { skip = false}
                r.push(i as i32); j += 1; if j == t.len() { break }
            }
        } if j == t.len() { r } else { vec![] }
    }
}

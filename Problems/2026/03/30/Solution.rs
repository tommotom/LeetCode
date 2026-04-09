impl Solution {
    pub fn check_strings(s1: String, s2: String) -> bool {
        let mut freq = vec![0 ;b'z' as usize +1];

        for skip in 0..2 {
            for x in s1.bytes().skip(skip).step_by(2) {freq[x as usize] +=1}
            for x in s2.bytes().skip(skip).step_by(2) {freq[x as usize] -=1}
            if !freq[b'a' as usize..].iter().all(|x| *x == 0) {return false}
        }
        return true;

    }
}

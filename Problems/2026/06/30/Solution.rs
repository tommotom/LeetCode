impl Solution {
    pub fn number_of_substrings(s: String) -> i32 {
        fn is_valid(counter: &Vec<i32>) -> bool {
            counter[0] > 0 && counter[1] > 0 && counter[2] > 0
        }
        let mut total = 0;
        let mut invalid = 0;
        let s: Vec<char> = s.chars().collect();
        let mut l = 0;
        let mut counter = vec![0; 3];
        for r in 0..s.len() {
            total += r + 1;
            let key = (s[r] as u8 - 'a' as u8) as usize;
            counter[key] += 1;
            while is_valid(&counter) {
                counter[(s[l] as u8 - 'a' as u8) as usize] -= 1;
                l += 1;
            }
            invalid += r - l + 1;
        }
        (total - invalid) as i32
    }
}

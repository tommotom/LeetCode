impl Solution {
    pub fn kth_character(k: i32) -> char {
        let k = k as usize;
        let mut arr = vec![0];
        while arr.len() <= k {
            let current_len = arr.len();
            for i in 0..current_len {
                arr.push((arr[i] + 1) % 26);
            }
        }
        ('a' as u8 + arr[k-1]) as char
    }
}
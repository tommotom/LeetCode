impl Solution {
    pub fn is_one_bit_character(bits: Vec<i32>) -> bool {
        let mut i = 0;
        while i < bits.len() - 1 {
            i += if bits[i] == 1 {2} else {1}
        }
        i == bits.len() - 1
    }
}

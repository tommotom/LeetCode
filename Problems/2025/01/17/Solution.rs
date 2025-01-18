impl Solution {
    pub fn does_valid_array_exist(derived: Vec<i32>) -> bool {
        let mut zero = 0;
        let mut one = 1;
        for i in 0..derived.len() {
            zero ^= derived[i];
            one ^= derived[i];
        }
        return zero == 0 || one == 1;
    }
}

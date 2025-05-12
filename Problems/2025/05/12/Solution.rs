use std::collections::HashSet;

impl Solution {
    pub fn find_even_numbers(digits: Vec<i32>) -> Vec<i32> {
        let mut set = HashSet::new();
        let n = digits.len();
        for i in 0..n {
            for j in 0..n {
                for k in 0..n {
                    if i == j || j == k || k == i {
                        continue;
                    }
                    if digits[i] == 0 || digits[k] % 2 == 1 {
                        continue;
                    }
                    set.insert(100 * digits[i] + 10 * digits[j] + digits[k]);
                }
            }
        }
        let mut vec = Vec::from_iter(set);
        vec.sort();
        vec
    }
}

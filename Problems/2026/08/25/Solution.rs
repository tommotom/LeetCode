use std::collections::HashSet;

impl Solution {
    pub fn missing_multiple(nums: Vec<i32>, k: i32) -> i32 {
        let mut set: HashSet<&i32> = HashSet::from_iter(nums.iter());
        let mut m = 1;
        loop {
            let num = k * m;
            if !set.contains(&num) {
                return num;
            }
            m += 1;
        }
        0
    }
}

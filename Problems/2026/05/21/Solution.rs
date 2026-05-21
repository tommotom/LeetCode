use std::collections::HashSet;

impl Solution {
    pub fn longest_common_prefix(arr1: Vec<i32>, arr2: Vec<i32>) -> i32 {
        let mut prefix = HashSet::new();
        for mut val in arr1 {
            while val > 0 {
                prefix.insert(val);
                val /= 10;
            }
        }

        let mut ans = 0;
        for mut val in arr2 {
            while val > 0 {
                if prefix.contains(&val) {
                    ans = ans.max(val.ilog10() + 1);
                    break;
                }
                val /= 10;
            }
        }
        ans as i32
    }
}

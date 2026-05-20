use std::collections::HashSet;

impl Solution {
    pub fn find_the_prefix_common_array(a: Vec<i32>, b: Vec<i32>) -> Vec<i32> {
        let mut a_set = HashSet::new();
        let mut b_set = HashSet::new();
        let mut both = HashSet::new();
        let mut ans = Vec::new();
        let mut count = 0;
        for i in 0..a.len() {
            a_set.insert(a[i]);
            b_set.insert(b[i]);
            if a_set.contains(&b[i]) {
                both.insert(b[i]);
            }
            if b_set.contains(&a[i]) {
                both.insert(a[i]);
            }
            ans.push(both.len() as i32);
        }
        ans
    }
}

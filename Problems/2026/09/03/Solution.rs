impl Solution {
    pub fn uniform_array(mut nums1: Vec<i32>) -> bool {
        nums1.sort();
        let mut min = nums1[0] % 2;
        let mut seen_odd = min == 1;
        for i in 1..nums1.len() {
            if !seen_odd && min != nums1[i] % 2 {
                return false;
            }
            seen_odd = seen_odd || nums1[i] % 2 == 1;
        }
        true
    }
}

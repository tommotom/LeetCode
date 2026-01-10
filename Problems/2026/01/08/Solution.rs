impl Solution {
    pub fn max_dot_product(nums1: Vec<i32>, nums2: Vec<i32>) -> i32 {
        let (m, n) = (nums1.len(), nums2.len());
        let mut cur = vec![i32::MIN; n+1];
        let mut prev = vec![i32::MIN; n+1];

        for i in 1..=m {
            for j in 1..=n {
                let p = nums1[i-1] * nums2[j-1];
                cur[j] = p.max(prev[j].max(cur[j-1].max(p + 0.max(prev[j-1]))));
            }
            std::mem::swap(&mut cur, &mut prev);
        }
        prev[n]
    }
}

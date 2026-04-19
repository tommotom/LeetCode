impl Solution {
    pub fn max_distance(nums1: Vec<i32>, nums2: Vec<i32>) -> i32 {
        let mut ans = 0;
        for i in 0..(nums1.len().min(nums2.len())) {
            let (mut l, mut r) = (i, nums2.len());
            while l < r {
                let m = l + (r - l) / 2;
                if nums1[i] > nums2[m] {
                    r = m;
                } else {
                    l = m + 1;
                }
            }
            if l > i {
                ans = ans.max((l - 1 - i) as i32);
            }
        }
        ans
    }
}

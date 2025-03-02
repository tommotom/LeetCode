impl Solution {
    pub fn merge_arrays(nums1: Vec<Vec<i32>>, nums2: Vec<Vec<i32>>) -> Vec<Vec<i32>> {
        let mut i1 = 0;
        let mut i2 = 0;
        let mut ans = Vec::new();
        while i1 < nums1.len() && i2 < nums2.len() {
            if nums1[i1][0] == nums2[i2][0] {
                ans.push(vec![nums1[i1][0], nums1[i1][1] + nums2[i2][1]]);
                i1 += 1;
                i2 += 1;
            } else if nums1[i1][0] < nums2[i2][0] {
                ans.push(nums1[i1].clone());
                i1 += 1;
            } else {
                ans.push(nums2[i2].clone());
                i2 += 1;
            }
        }
        while i1 < nums1.len() {
            ans.push(nums1[i1].clone());
            i1 += 1;
        }
        while i2 < nums2.len() {
            ans.push(nums2[i2].clone());
            i2 += 1;
        }
        ans
    }
}

impl Solution {
    pub fn kth_smallest_product(nums1: Vec<i32>, nums2: Vec<i32>, k: i64) -> i64 {
        let (neg1, pos1): (Vec<i32>, Vec<i32>) = nums1.iter().partition(|&&x| x < 0);
        let (neg2, pos2): (Vec<i32>, Vec<i32>) = nums2.iter().partition(|&&x| x < 0);
        let rneg1: Vec<i32> = neg1.iter().cloned().rev().collect();
        let rneg2: Vec<i32> = neg2.iter().cloned().rev().collect();
        let rpos1: Vec<i32> = pos1.iter().cloned().rev().collect();
        let rpos2: Vec<i32> = pos2.iter().cloned().rev().collect();
        let countle = |mid: i64| {
            Solution::countle_in_sorted_matrix(&neg1, &rpos2, mid)
                + Solution::countle_in_sorted_matrix(&rneg1, &rneg2, mid)
                + Solution::countle_in_sorted_matrix(&rpos1, &neg2, mid)
                + Solution::countle_in_sorted_matrix(&pos1, &pos2, mid)
        };

        let limit = 10_i64.pow(10);
        let mut r = (-limit, limit);
        while r.0 != r.1 {
            let mid = r.0 + (r.1 - r.0) / 2;
            if countle(mid) < k {
                r.0 = mid + 1;
            } else {
                r.1 = mid;
            }
        }
        r.0
    }

    fn countle_in_sorted_matrix(nums1: &[i32], nums2: &[i32], k: i64) -> i64 {
        let mut j = nums2.len();
        let mut cnt: i64 = 0;
        for &v in nums1 {
            while j != 0 && (nums2[j - 1] as i64) * (v as i64) > k {
                j -= 1;
            }
            cnt += j as i64;
        }

        cnt
    }
}

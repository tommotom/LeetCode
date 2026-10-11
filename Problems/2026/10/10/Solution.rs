impl Solution {
    pub fn min_sum_square_diff(mut nums1: Vec<i32>, nums2: Vec<i32>, k1: i32, k2: i32) -> i64 {
        let n = nums1.len();
        let mut k = k1 as i64 + k2 as i64;

        let mut sum = 0i64;
        for i in 0..n {
            nums1[i] = (nums1[i] - nums2[i]).abs();
            sum += nums1[i] as i64;
        }
        if sum <= k {
            return 0;
        }

        nums1.sort_unstable_by(|a, b| b.cmp(a));
        nums1.push(0);

        for i in 1..=n {
            let cost = (nums1[i - 1] - nums1[i]) as i64 * i as i64;
            if cost > k {
                let (q, r) = (k / i as i64, k % i as i64);
                let hi = nums1[i - 1] as i64 - q;
                let mut ans = hi * hi * (i as i64 - r) + (hi - 1) * (hi - 1) * r;
                for &x in &nums1[i..n] {
                    ans += x as i64 * x as i64;
                }
                return ans;
            }
            k -= cost;
        }
        0
    }
}

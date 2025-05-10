impl Solution {
    pub fn min_sum(nums1: Vec<i32>, nums2: Vec<i32>) -> i64 {
        fn count(nums: Vec<i32>) -> (i32, i64) {
            let mut zeros = 0;
            let mut sum = 0;
            for num in nums {
                if num == 0 {
                    sum += 1 as i64;
                    zeros += 1;
                } else {
                    sum += num as i64;
                }
            }
            (zeros, sum)
        }

        let (zeros1, sum1) = count(nums1);
        let (zeros2, sum2) = count(nums2);

        if (sum1 > sum2 && zeros2 == 0) || (sum1 < sum2 && zeros1 == 0) {
            return -1;
        }

        sum1.max(sum2)
    }
}

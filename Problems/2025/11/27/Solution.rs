impl Solution {
    pub fn max_subarray_sum(nums: Vec<i32>, k: i32) -> i64 {
        let k = k as usize;

        let mut min_prefix = vec![i64::MAX / 2; k];
        min_prefix[k - 1] = 0;

        let mut prefix: i64 = 0;
        let mut ans: i64 = i64::MIN;

        for (i, x) in nums.into_iter().enumerate() {
            prefix += x as i64;
            let r = i % k;
            ans = ans.max(prefix - min_prefix[r]);
            if prefix < min_prefix[r] {
                min_prefix[r] = prefix;
            }
        }

        ans
    }
}

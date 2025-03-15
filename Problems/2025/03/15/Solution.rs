impl Solution {
    pub fn min_capability(nums: Vec<i32>, k: i32) -> i32 {
        fn isValid(nums: &Vec<i32>, m: i32, k: i32) -> bool {
            let mut count = 0;
            let mut i = 0;
            while i < nums.len() {
                if nums[i] <= m {
                    count += 1;
                    i += 1;
                }
                i += 1;
            }
            count >= k
        }

        let mut l = 1;
        let mut r = *nums.iter().max().unwrap();
        while l < r {
            let m = l + (r - l) / 2;
            if isValid(&nums, m, k) {
                r = m
            } else {
                l = m + 1;
            }
        }
        l
    }
}

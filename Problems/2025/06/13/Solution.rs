impl Solution {
    pub fn minimize_max(mut nums: Vec<i32>, p: i32) -> i32 {
        fn count(nums: &Vec<i32>, diff: i32) -> i32 {
            let mut count = 0;
            let mut i = 0;
            while i+1 < nums.len() {
                if (nums[i] - nums[i+1]).abs() <= diff {
                    count += 1;
                    i += 2;
                } else {
                    i += 1;
                }
            }
            return count;
        }

        nums.sort();
        let mut l = 0; let mut r = i32::MAX;
        while l < r {
            let m = l + (r - l) / 2;
            if count(&nums, m) < p {
                l = m + 1;
            } else {
                r = m;
            }
        }
        l
    }
}

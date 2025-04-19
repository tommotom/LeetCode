impl Solution {
    pub fn count_fair_pairs(mut nums: Vec<i32>, lower: i32, upper: i32) -> i64 {
        fn bisect_lower(nums: &Vec<i32>, target: i32) -> i64 {
            let mut l = 0;
            let mut r = nums.len();
            while l < r {
                let m = l + (r - l) / 2;
                if nums[m] < target {
                    l = m + 1;
                } else {
                    r = m;
                }
            }
            l as i64
        }

        fn bisect_upper(nums: &Vec<i32>, target: i32) -> i64 {
            let mut l = 0;
            let mut r = nums.len();
            while l < r {
                let m = l + (r - l) / 2;
                if nums[m] <= target {
                    l = m + 1;
                } else {
                    r = m;
                }
            }
            l as i64
        }

        nums.sort();
        let mut ans = 0;
        for i in 1..nums.len() {
            let l = bisect_lower(&nums, lower - nums[i]).min(i as i64);
            let u = bisect_upper(&nums, upper - nums[i]).min(i as i64);
            ans += (u - l).max(0);
        }

        ans
    }
}

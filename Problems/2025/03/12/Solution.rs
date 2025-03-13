impl Solution {
    pub fn maximum_count(nums: Vec<i32>) -> i32 {
        fn bisect(nums: &Vec<i32>, target: i32) -> usize {
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
            l
        }

        let neg = bisect(&nums, 0);
        let pos = nums.len() - bisect(&nums, 1);

        pos.max(neg) as i32
    }
}

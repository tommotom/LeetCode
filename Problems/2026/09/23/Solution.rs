impl Solution {
    pub fn min_operations(nums: Vec<i32>, x: i32) -> i32 {
        let mut target: i32 = -x;
        let n = nums.len() as i32;

        for &num in &nums {
            target += num;
        }

        if target == 0 {
            return n;
        }

        let (mut max_len, mut cur_sum, mut left) = (0, 0, 0);

        for right in 0..n as usize {
            cur_sum += nums[right];
            while left <= right as i32 && cur_sum > target {
                cur_sum -= nums[left as usize];
                left += 1;
            }
            if cur_sum == target {
                max_len = std::cmp::max(max_len, right as i32 - left + 1);
            }
        }

        if max_len != 0 { n - max_len } else { -1 }
    }
}

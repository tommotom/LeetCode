impl Solution {
    pub fn missing_integer(mut nums: Vec<i32>) -> i32 {
        let mut target = nums[0];
        for i in 1..nums.len() {
            if nums[i-1] + 1 == nums[i] {
                target += nums[i];
            } else {
                break;
            }
        }
        nums.sort();
        for num in nums {
            if num < target {
                continue;
            } else if num == target {
                target += 1;
            } else {
                return target;
            }
        }
        target
    }
}

use std::collections::HashMap;

impl Solution {
    pub fn find_target_sum_ways(nums: Vec<i32>, target: i32) -> i32 {
        let mut memo = HashMap::new();
        Self::helper(&nums, 0, target, &mut memo)
    }

    fn helper(nums: &Vec<i32>, i: usize, sum: i32, memo: &mut HashMap<(usize, i32), i32>) -> i32 {
        if nums.len() == i {
            return if sum == 0 { 1 } else { 0 };
        }
        let key = (i, sum);
        if let Some(&val) = memo.get(&key) {
            return val;
        }
        let add = Self::helper(nums, i + 1, sum + nums[i], memo);
        let subtract = Self::helper(nums, i + 1, sum - nums[i], memo);
        let val = add + subtract;
        memo.insert(key, val);
        val
    }
}

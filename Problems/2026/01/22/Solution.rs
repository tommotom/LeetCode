impl Solution {
    pub fn minimum_pair_removal(mut nums: Vec<i32>) -> i32 {
        fn is_non_decreasing(nums: &Vec<i32>) -> bool {
            for i in 1..nums.len() {
                if nums[i-1] > nums[i] {
                    return false;
                }
            }
            true
        }

        let mut ans = 0;
        while !is_non_decreasing(&nums) {
            let mut minimum = i32::MAX;
            let mut i = 0;
            for j in 1..nums.len() {
                let sum = nums[j-1] + nums[j];
                if minimum > sum {
                    minimum = sum;
                    i = j;
                }
            }
            nums.remove(i);
            nums[i - 1] = minimum;
            ans += 1;
        }
        ans
    }
}

impl Solution {
    pub fn check(nums: Vec<i32>) -> bool {
        let n = nums.len();
        let mut count = if nums[0] < nums[n-1] {1} else {0};
        for i in 1..n {
            if nums[i-1] > nums[i] {
                count += 1;
            }
        }
        count <= 1
    }
}

impl Solution {
    pub fn check(nums: Vec<i32>) -> bool {
        let n = nums.len();
        let mut count = 0;
        for i in 1..n {
            if nums[i] < nums[i-1] {
                count += 1;
            }
        }

        if nums[0] < nums[n-1] {
            count += 1;
        }

        count <= 1
    }
}

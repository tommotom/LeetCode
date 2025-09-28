impl Solution {
    pub fn largest_perimeter(mut nums: Vec<i32>) -> i32 {
        nums.sort();
        let mut ans = 0;
        for i in 0..(nums.len()-2) {
            if nums[i] + nums[i+1] > nums[i+2] {
                ans = ans.max(nums[i] + nums[i+1] + nums[i+2]);
            }
        }
        ans
    }
}

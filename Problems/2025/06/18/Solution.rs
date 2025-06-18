impl Solution {
    pub fn divide_array(mut nums: Vec<i32>, k: i32) -> Vec<Vec<i32>> {
        nums.sort();
        let mut i = 0;
        let mut ans = Vec::new();
        while i < nums.len() {
            if nums[i+2] - nums[i] > k {
                return Vec::new();
            }
            ans.push([nums[i], nums[i+1], nums[i+2]].to_vec());
            i += 3;
        }
        ans
    }
}

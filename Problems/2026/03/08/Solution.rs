impl Solution {
    pub fn find_different_binary_string(nums: Vec<String>) -> String {
        let nums: Vec<Vec<char>> = nums.iter().map(|num| num.chars().collect()).collect();
        let mut ans = Vec::new();
        for i in 0..nums.len() {
            ans.push(if nums[i][i] == '1' {"0"} else {"1"});
        }
        ans.join("")
    }
}

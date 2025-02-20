impl Solution {
    pub fn find_different_binary_string(nums: Vec<String>) -> String {
        nums.into_iter().enumerate().map(|(i, s)| {
            if s.chars().nth(i).unwrap() == '0' {'1'} else {'0'}
        }).collect()
    }
}

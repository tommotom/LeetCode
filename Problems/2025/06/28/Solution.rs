impl Solution {
    pub fn max_subsequence(nums: Vec<i32>, k: i32) -> Vec<i32> {
        let mut arr = Vec::new();
        for i in 0..nums.len() {
            arr.push((nums[i], i));
        }
        arr.sort_by(|a, b| b.0.cmp(&a.0));
        let mut ans = Vec::new();
        for i in 0..k {
            ans.push(arr[i as usize]);
        }
        ans.sort_by(|a, b| a.1.cmp(&b.1));
        ans.iter().map(|a| a.0).collect()
    }
}

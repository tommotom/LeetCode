impl Solution {
    pub fn minimum_abs_difference(mut arr: Vec<i32>) -> Vec<Vec<i32>> {
        arr.sort();
        let mut diff = i32::MAX;
        for i in 1..arr.len() {
            diff = diff.min(arr[i] - arr[i-1]);
        }
        let mut ans = Vec::new();
        for i in 1..arr.len() {
            if arr[i] - arr[i-1] == diff {
                ans.push(vec![arr[i-1], arr[i]]);
            }
        }
        ans
    }
}

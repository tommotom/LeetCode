impl Solution {
    pub fn find_lucky(arr: Vec<i32>) -> i32 {
        let mut freq = vec![0; 501];
        for &num in &arr {
            let i = num as usize;
            freq[i] += 1;
        }
        let mut ans = -1;
        for &num in &arr {
            let i = num as usize;
            if num == freq[i] {
                ans = ans.max(num);
            }
        }
        ans
    }
}

impl Solution {
    pub fn min_deletion_size(strs: Vec<String>) -> i32 {
        let strs: Vec<Vec<char>> = strs.into_iter().map(|s| s.chars().collect()).collect();
        let mut ans = 0;
        for j in 0..strs[0].len() {
            for i in 1..strs.len() {
                if strs[i-1][j] > strs[i][j] {
                    ans += 1;
                    break;
                }
            }
        }
        ans
    }
}

impl Solution {
    pub fn min_deletion_size(strs: Vec<String>) -> i32 {
        let strs: Vec<Vec<char>> = strs.into_iter().map(|s| s.chars().collect()).collect();
        let n = strs.len();
        let m = strs[0].len();
        let mut cuts = vec![false; n-1];

        let mut ans = 0;
        for j in 0..m {
            let mut b = false;
            for i in 1..n {
                if !cuts[i-1] && strs[i-1][j] > strs[i][j] {
                    ans += 1;
                    b = true;
                    break;
                }
            }
            if b {
                continue;
            }
            for i in 1..n {
                if strs[i-1][j] < strs[i][j] {
                    cuts[i-1] = true;
                }
            }
        }
        ans
    }
}

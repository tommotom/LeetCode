impl Solution {
    pub fn find_diagonal_order(mat: Vec<Vec<i32>>) -> Vec<i32> {
        let (m, n) = (mat.len(), mat[0].len());
        let (mut r, mut c) = (0, 0);
        let mut ans = Vec::new();
        while 0 <= r && r < m && 0 <= c && c < n {
            ans.push(mat[r][c]);
            if (r + c) % 2 == 0 {
                if c == n-1 {
                    r += 1;
                } else if r == 0 {
                    c += 1;
                } else {
                    r -= 1;
                    c += 1;
                }
            } else {
                if r == m-1 {
                    c += 1;
                } else if c == 0 {
                    r += 1;
                } else {
                    r += 1;
                    c -= 1;
                }
            }
        }
        ans
    }
}

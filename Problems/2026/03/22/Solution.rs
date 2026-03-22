impl Solution {
    pub fn find_rotation(mat: Vec<Vec<i32>>, target: Vec<Vec<i32>>) -> bool {
        let mut m = mat.len();
        let mut n = mat[0].len();
        let mut a = target.len() == m && target[0].len() == n;
        let mut b = target.len() == n && target[0].len() == m;
        let mut cc = target.len() == m && target[0].len() == n;
        let mut d = target.len() == n && target[0].len() == m;
        for r in 0..m {
            for c in 0..n {
                if a && mat[r][c] != target[r][c] {
                    a = false;
                }
                if b && mat[r][c] != target[c][target[0].len() - r - 1] {
                    b = false;
                }
                if cc && mat[r][c] != target[target.len() - r - 1][target[0].len() - c - 1] {
                    cc = false;
                }
                if d && mat[r][c] != target[target.len() - c - 1][r] {
                    d = false;
                }
            }
        }
        a || b || cc || d
    }
}

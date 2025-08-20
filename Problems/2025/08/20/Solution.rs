impl Solution {
    pub fn count_squares(matrix: Vec<Vec<i32>>) -> i32 {
        let (n, m) = (matrix.len(), matrix[0].len());
        let mut ans = 0;
        for i in 0..n {
            for j in 0..m {
                if matrix[i][j] == 0 {
                    continue;
                }
                ans += 1;
                for side in 2..((n-i+1).min(m-j+1)) {
                    let mut isValid = true;
                    for d in 0..side {
                        if matrix[i+side-1][j+d] == 0 || matrix[i+d][j+side-1] == 0 {
                            isValid = false;
                            break;
                        }
                    }
                    if isValid {
                        ans += 1;
                    } else {
                        break;
                    }
                }
            }
        }
        ans
    }
}

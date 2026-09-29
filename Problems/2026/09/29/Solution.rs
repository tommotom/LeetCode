impl Solution {
    pub fn has_valid_path(grid: Vec<Vec<char>>) -> bool {
        if grid[0][0] == ')' {
            return false;
        }
        let (m, n) = (grid.len(), grid[0].len());
        let max = m + n;
        let mut depth = vec![vec![vec![false; max]; n]; m];
        depth[0][0][1] = true;
        for r in 0..m {
            for c in 0..n {
                if r > 0 {
                    for d in 0..max {
                        if grid[r][c] == '(' {
                            if d > 0 && depth[r-1][c][d-1] {
                                depth[r][c][d] = true;
                            }
                        }
                        if grid[r][c] == ')' {
                            if d + 1 < max && depth[r-1][c][d+1] {
                                depth[r][c][d] = true;
                            }
                        }
                    }
                }
                if c > 0 {
                    for d in 0..max {
                        if grid[r][c] == '(' {
                            if d > 0 && depth[r][c-1][d-1] {
                                depth[r][c][d] = true;
                            }
                        }
                        if grid[r][c] == ')' {
                            if d + 1 < max && depth[r][c-1][d+1] {
                                depth[r][c][d] = true;
                            }
                        }
                    }
                }
            }
        }
        depth[m-1][n-1][0]
    }
}
